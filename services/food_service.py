from typing import List, Optional
from domain.models import Food, Ingredient
from infrastructure.sql_repository import SQLFoodRepository

class FoodService:
    """
    FoodService is a service class responsible for managing food-related operations. 
    It acts as an intermediary between the application logic and the data repository.

    Attributes:
        repository (SQLFoodRepository): An instance of SQLFoodRepository used to interact 
        with the underlying data storage for food-related data.

    Args:
        repository (SQLFoodRepository): The data repository instance that provides 
        methods for accessing and manipulating food data.
    """
    def __init__(self,repository: SQLFoodRepository):
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
    
    def calculate_meal(self, ingredients: List[Ingredient]) -> dict:
        total_prot = 0
        total_carb = 0
        total_fats = 0

        missing = []

        for item in ingredients:
            food = self.get_food_by_name(item.name)
            if not food:
                missing.append(item.name)
                continue

            ratio = item.weight_g/100

            total_prot += food.protein_per_100g * ratio
            total_fats  += food.fats_per_100g * ratio
            total_carb += food.carbs_per_100g * ratio
        return{
            "total_protein": total_prot,
            "total_carbs": total_carb,
            "total_fats": total_fats,
            "missing_foods": missing
        }