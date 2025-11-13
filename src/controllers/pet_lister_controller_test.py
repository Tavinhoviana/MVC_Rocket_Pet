from src.models.sqlite.entitites.pets import PetsTable
from .pet_lister_controller import PetsListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="fluffy", type="cat", id=4),
            PetsTable(name="buddy", type="dog", id=7)
        ]

def test_list_pets():
    controller = PetsListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                { "name": "fluffy", "id": 4 },
                { "name": "buddy", "id": 7 }
            ]
        }
    }

    assert response == expected_response
