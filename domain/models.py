from dataclasses import dataclass
from pydantic import BaseModel
@dataclass
class Food:
    CALS_PER_GRAM_CARBS = 4
    CALS_PER_GRAM_PROTEIN = 4
    CALS_PER_GRAM_FATS = 9
    name:str
    protein_per_100g: float
    carbs_per_100g: float
    fats_per_100g: float
    def __post_init__(self):
            if self.protein_per_100g < 0 or self.carbs_per_100g < 0 or self.fats_per_100g < 0:
                raise ValueError("Nutritional values must be non-negative.")

    @property
    def calories_per_100g(self): 
        return (self.carbs_per_100g * self.CALS_PER_GRAM_CARBS + 
                self.protein_per_100g * self.CALS_PER_GRAM_PROTEIN + 
                self.fats_per_100g * self.CALS_PER_GRAM_FATS)
    
    def calculate_calories(self, grams: float) -> float:
        if grams < 0:
             raise ValueError("Weight in grams must be non-negative.")
        return (grams / 100) * self.calories_per_100g
    
class Ingredient(BaseModel):
     name:str
     weigtht_g: float
    
    

