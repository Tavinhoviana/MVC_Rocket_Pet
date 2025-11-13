from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entitites.pets import PetsTable

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
