from typing import Dict, List
from config.config import cow_collection
from model.cow import Cow, cow_decoder
from bson.objectid import ObjectId

def insert_cow(serialised_cow: Dict) -> int:
    return cow_collection.insert_one(serialised_cow).inserted_id

def get_cows() -> List[Cow]:
    dict_list: List[Dict] = list(cow_collection.find())
    cow_list: List[Cow] = list()

    for cow_dict in dict_list:
        del cow_dict["_id"]
        cow_list.append(cow_decoder(cow_dict))

    print(cow_list)
    return cow_list


def delete_cow(cow_id: int) -> bool:
    return cow_collection.delete_one({'_id': ObjectId(cow_id)}).deleted_count > 0


def update_cow(cow_id: int, updating_cow: Cow) -> int:
    return cow_collection.update_one({'_id': ObjectId(cow_id)}, { "$set": updating_cow.serialize() }).modified_count > 0
