# Cows API
from typing import List, Dict, Tuple
from config.config import app, v1_registry, rebar, mimetype_json

from flask import jsonify, request, Response

from model.cow import Cow, cow_decoder
import traceback
import json

import persistence.cow_repository as cow_repository

# Designer note: We could use libraries as `https://apispec.readthedocs.io/en/latest/index.html` for generating
# OpenAPI v3 specs (swagger)

@v1_registry.handles("/cows", method="GET")
def get_cows() -> Response:
    cow_dict_list: List[Dict] = list()
    query = request.args.get("q")

    filtered_cow_list: List[Cow] = filter_cows(query, cow_repository.get_cows())

    for cow in filtered_cow_list:
        cow_dict = cow.serialize().copy()
        cow_dict_list.append(cow_dict)

    return jsonify([cow for cow in cow_dict_list])


@v1_registry.handles("/cows", method="POST")
def insert_cow() -> Response:
    input_json: str = request.get_json()

    if input_json is None:
        return Response(jsonify(isError=True,
                        message="Input error",
                        statusCode=400,
                        data="No cows were provided").data, status=400, mimetype=mimetype_json)

    try:
        cow_dict = json.loads(json.dumps(input_json))
        new_cow = cow_decoder(cow_dict)
    except:
        traceback.print_exc()  # These kind of traces could be sent to an external system, like MS Application Insights
        return Response(jsonify(isError=True,
                                message="Input error",
                                statusCode=400,
                                data="Cow schema was incorrect").data, status=400, mimetype=mimetype_json)

    new_cow_id = cow_repository.insert_cow(new_cow.serialize())
    return Response(jsonify(id=str(new_cow_id)).data, status=201, mimetype=mimetype_json)


@v1_registry.handles("/cows/<cow_id>", method="PUT")
def update_cow(cow_id: str) -> Response:
    if cow_id is None:
        return Response(jsonify(isError=True,
                                message="Input error",
                                statusCode=400,
                                data="No ID was provided").data, status=400, mimetype=mimetype_json)

    input_json = request.get_json()

    if input_json is None:
        return Response(jsonify(isError=True,
                                message="Input error",
                                statusCode=400,
                                data="No cows were provided").data, status=400, mimetype=mimetype_json)

    cow_dict = json.loads(json.dumps(input_json))
    updating_cow: Cow = cow_decoder(cow_dict)

    updated = cow_repository.update_cow(cow_id, updating_cow)

    if updated:
        return Response(None, status=200, mimetype=mimetype_json)
    else:
        return Response(None, status=404, mimetype=mimetype_json)


@v1_registry.handles("/cows/<cow_id>", method="DELETE")
def delete_cow(cow_id: str) -> Response:
    if cow_id is None:
        return Response(jsonify(isError=True,
                                message="Input error",
                                statusCode=400,
                                data="No ID was provided").data, status=400, mimetype=mimetype_json)

    deleted = cow_repository.delete_cow(cow_id)

    if deleted:
        return Response(None, status=200, mimetype=mimetype_json)
    else:
        return Response(None, status=404, mimetype=mimetype_json)


# This filter should be moved to MongoDB filters to increase performance
def filter_cows(query: str, cows: List[Cow]) -> List[Cow]:
    filtered_list: List[Cow] = list()
    query_terms: List[Tuple] = list()
    if query is None:
        return cows
    else:
        elem_list = query.split(";")
        for elem in elem_list:
            term_pair = elem.split(":")
            query_terms.append((term_pair[0], term_pair[1]))

        for cow in cows:
            cow_dict = cow.__dict__
            for query_tuple in query_terms:
                if (cow_dict[query_tuple[0]] is not None) and str(cow_dict[query_tuple[0]]) == str(query_tuple[1]):
                    filtered_list.append(cow)

    return filtered_list


rebar.init_app(app)
