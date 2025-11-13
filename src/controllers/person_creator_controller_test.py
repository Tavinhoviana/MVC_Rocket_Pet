import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():
    person_info = {
        "first_name": "guinga",
        "last_name": "Cancuners",
        "age": 33,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response["data"]["types"] == "person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "first_name": "guinga666",
        "last_name": "Cancuners",
        "age": 33,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
