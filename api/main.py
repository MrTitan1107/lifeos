from fastapi import FastAPI, HTTPException
from typing import List
from domain.models import Food
from infrastructure.repositories import CSVRepository
from services.food_services import FoodService

app = FastAPI(title="LifeOS")

repo = CSVRepository(file_path="data/foods.csv")

service = FoodService(repository=repo)


@app.get("/foods", response_model=List[Food])
def get_foods():
    try:
        return service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@app.post("/foods")
def create_food(food: Food):
    """
    Recibe un JSON, lo convierte a objeto Food, valida los tipos
    y lo guarda en el CSV.
    """
    try:
        service.create_food(food)
        return {"message": "Alimento creado correctamente", "data": food}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/foods/{name}", response_model=Food)
def get_food_by_name(name: str):
    food = service.get_food_by_name(name)
    if not food:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")
    return food



@app.delete("/foods/{food_name}")
def delete_food(food_name:str):
    """
    Elimina un alimento a partir de su nombre.
    """
    if not service.get_food_by_name(food_name):
        raise HTTPException(status_code=404, detail= f"Alimento \"{food_name}\" no encontrado")
    service.delete_food(food_name)
    return {"message": f"Alimento \"{food_name}\" eliminado correctamente"}