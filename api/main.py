from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

# Importamos tus piezas de LEGO
from domain.models import Food, Ingredient
from services.food_service import FoodService
from infrastructure.database import SessionLocal, engine, Base
from infrastructure.entities import FoodEntity
from infrastructure.sql_repository import SQLFoodRepository

# 1. CREAR LAS TABLAS (Si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LifeOS")

# --- ZONA DE DEPENDENCIAS (La Fábrica de Objetos) ---

# Esta función se encarga de abrir y cerrar la conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # ¡Muy importante! Cierra el grifo al terminar.

# Esta función fabrica el SERVICIO listo para usar
# Pide la base de datos (db) -> Crea el Repo -> Crea el Service
def get_service(db: Session = Depends(get_db)) -> FoodService:
    repository = SQLFoodRepository(db)
    return FoodService(repository)

# --- ENDPOINTS ---

@app.get("/foods", response_model=List[Food])
# Fíjate: Ya no usamos la variable global 'service'.
# Ahora pedimos "service: FoodService = Depends(get_service)"
def get_all_foods(service: FoodService = Depends(get_service)):
    return service.get_all()

@app.post("/foods")
def create_food(food: Food, service: FoodService = Depends(get_service)):
    try:
        service.create_food(food)
        return {"message": "Alimento creado correctamente", "data": food}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/foods/{name}", response_model=Food)
def get_food_by_name(name: str, service: FoodService = Depends(get_service)):
    food = service.get_food_by_name(name)
    if not food:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")
    return food

@app.delete("/foods/{food_name}")
def delete_food(food_name: str, service: FoodService = Depends(get_service)):
    if not service.get_food_by_name(food_name):
        raise HTTPException(status_code=404, detail=f"Alimento {food_name} no encontrado")
    
    service.delete_food(food_name)
    # service.delete_food(food_name) <--- Descomenta si lo tienes implementado
    return {"message": f"Alimento {food_name} eliminado correctamente"} 

@app.post("/meal/calculate")
def calculate_meal_macros(ingredients: List[Ingredient], service: FoodService = Depends(get_service)):
    """
    Calculadora nutricional.
    """
    results = service.calculate_meal(ingredients)
    return results
