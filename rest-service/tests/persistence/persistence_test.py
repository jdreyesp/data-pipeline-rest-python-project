import controller.controller as controller
import json
from model.cow import Cow
from typing import Dict


def test_should_insert_a_cow_when_serialised_cow_is_provided():
    assert True


def test_should_not_insert_a_cow_when_not_serialised_cow_is_provided():
    assert True

def test_should_get_all_cows():
    assert True

def test_should_filter_a_cow():
    assert True

def test_should_update_a_cow():
    assert True


# This functional requirement will be assumed here, this would be confirmed with PO
def test_should_not_update_a_cow_when_given_fields_not_allowed_for_schema():
    assert True

def test_should_not_update_a_cow_when_cow_id_does_not_exists():
    assert True

def test_should_delete_an_existing_cow():
    assert True

def test_should_not_delete_a_cow_when_cow_id_does_not_exists():
    assert True
