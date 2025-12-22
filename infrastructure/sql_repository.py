from sqlalchemy.orm import Session
from typing import List, Optional
from domain.models import Food
from infrastructure.entities import FoodEntity

class SQLFoodRepository:
    def __init__(self, session: Session):
        # En lugar de un nombre de archivo, recibimos una sesión de base de datos activa
        self.session = session

    def save(self, food: Food) -> Food:
        # 1. TRADUCCIÓN: Pydantic -> Entity
        # Creamos la ficha para la base de datos
        food_entity = FoodEntity(
            name=food.name,
            protein_per_100g=food.protein_per_100g,
            carbs_per_100g=food.carbs_per_100g,
            fats_per_100g=food.fats_per_100g
        )

        # 2. GUARDAR
        self.session.add(food_entity)
        self.session.commit()      # Confirmamos la operación
        self.session.refresh(food_entity) # Recargamos para obtener el ID nuevo
        
        # 3. ACTUALIZAR EL ORIGINAL
        # Le ponemos el ID que la base de datos acaba de generar
        food.id = food_entity.id
        return food

    def get_all(self) -> List[Food]:
        # 1. LEER DE LA BD
        # "Dame todos los objetos de la tabla FoodEntity"
        entities = self.session.query(FoodEntity).all()
        
        # 2. TRADUCCIÓN: Entity -> Pydantic
        # Convertimos cada resultado de la BD en un objeto limpio para el servicio
        return [
            Food(
                id=e.id,
                name=e.name,
                protein_per_100g=e.protein_per_100g,
                carbs_per_100g=e.carbs_per_100g,
                fats_per_100g=e.fats_per_100g
            )
            for e in entities
        ]

    def find_by_name(self, name: str) -> Optional[Food]:
        # Buscamos el PRIMERO que coincida con el nombre
        entity = self.session.query(FoodEntity).filter(FoodEntity.name == name).first()
        
        if not entity:
            return None
            
        return Food(
            id=entity.id,
            name=entity.name,
            protein_per_100g=entity.protein_per_100g,
            carbs_per_100g=entity.carbs_per_100g,
            fats_per_100g=entity.fats_per_100g
        )
    
    def find_by_id(self, food_id: int) -> Optional[Food]:
        entity = self.session.query(FoodEntity).filter(FoodEntity.id == food_id).first()
        
        if not entity:
            return None
            
        return Food(
            id=entity.id,
            name=entity.name,
            protein_per_100g=entity.protein_per_100g,
            carbs_per_100g=entity.carbs_per_100g,
            fats_per_100g=entity.fats_per_100g
        )
    
    def delete(self, name:str) -> None:
        entity = self.session.query(FoodEntity).filter(FoodEntity.name == name).first()
        
        if entity:
            self.session.delete(entity)
            self.session.commit()