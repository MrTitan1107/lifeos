from typing import Optional
from pydantic import BaseModel

class Food(BaseModel):
    # 1. EL ID NUEVO: Opcional, porque al crear un alimento nuevo aún no tiene número.
    # Pero cuando viene de la base de datos, sí lo tendrá.
    id: Optional[int] = None
    
    name: str
    protein_per_100g: float
    carbs_per_100g: float
    fats_per_100g: float

    # 2. EL ENCHUFE MÁGICO (Config):
    # Esto permite que Pydantic lea los objetos "raros" que devuelve SQLAlchemy (ORM)
    # y los convierta a JSON automáticamente.
    class Config:
        from_attributes = True

class Ingredient(BaseModel):
    name: str
    weight_g: float  # <--- Corregido el typo "weigtht"
    

