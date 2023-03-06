import controller.controller as controller
import json
from model.cow import Cow
from typing import Dict


def test_should_get_correct_response_on_get():
    with controller.app.app_context():
        # Given
        # A set of cows

        # When
        cows = controller.get_cows()

        # Then
        assert cows.status_code == 200


def test_should_insert_a_cow():
    # Given
    # A cow
    cow_json_str: Dict = json.dumps(Cow(1, "Matilda", "Female").__dict__, indent=4)
    print(cow_json_str)

    with controller.app.test_request_context("/cows", method="POST", data=cow_json_str):
        # When
        cows = controller.insert_cow()

        # Then
        assert cows.status_code == 201
        assert "id" in cows.data


def test_should_give_400_when_wrong_schema_is_provided():
    assert True


def test_should_give_an_unique_id_when_inserting_cows():
    assert True


def test_should_return_400_when_no_id_is_provided_when_updating_cow():
    assert True


def test_should_return_404_when_no_cow_is_found_when_updating_cow():
    assert True


def test_should_update_cow():
    assert True


def test_should_return_400_when_no_id_is_provided_when_deleting_cow():
    assert True


def test_should_return_404_when_no_cow_is_found_when_deleting_cow():
    assert True


def test_should_filter_by_single_statement_in_query():
    assert True


def test_should_filter_by_multiple_statements_in_query():
    assert True


def test_should_return_same_list_when_no_query_is_provided():
    assert True
