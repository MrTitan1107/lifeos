from typing import List, Optional
from domain.models import Food
from infrastructure.repositories import CSVRepository

class FoodService:
    """
    FoodService is a service class responsible for managing food-related operations. 
    It acts as an intermediary between the application logic and the data repository.

    Attributes:
        repository (CSVRepository): An instance of CSVRepository used to interact 
        with the underlying data storage for food-related data.

    Args:
        repository (CSVRepository): The data repository instance that provides 
        methods for accessing and manipulating food data.
    """
    def __init__(self,repository: CSVRepository):
        self.repository = repository

    def get_all(self) -> List[Food]:
        return self.repository.get_all()
    
    def create_food(self, food: Food) -> Food:
        existing_food = self.repository.find_by_name(food.name)
        if existing_food:
            raise ValueError(f"El alimento {food.name} ya existe")
        self.repository.save(food)
        return food
    
    def get_food_by_name(self, name:str) -> Optional[Food]:
        return self.repository.find_by_name(name)
    
    def delete_food(self, name:str) -> None:
        return self.repository.delete(name)