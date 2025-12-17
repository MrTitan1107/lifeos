from fastapi import FastAPI, HTTPException
from typing import List
from domain.models import Food
from infrastructure.repositories import CSVRepository

app = FastAPI(titel="LifeOS")

repo = CSVRepository(file_path="data/foods.csv")

@app.get("/foods", response_model=List[Food])
def get_foods():
    return repo.get_all()

@app.post("/foods")
def create_food(food: Food):
    """
    Recibe un JSON, lo convierte a objeto Food, valida los tipos
    y lo guarda en el CSV.
    """
    repo.save(food)
    return {"message": "Alimento creado correctamente", "data": food}
@app.get("/foods/{name}", response_model=Food)
def get_food_by_name(name: str):
    food = repo.find_by_name(name)
    if not food:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")
    return food

@app.delete("/foods/{name}")
def delete_food(name:str):
    """
    Elimina un alimento a partir de su nombre.
    """
    if not repo.find_by_name(name):
        raise HTTPException(status_code=404, detail= f"Alimento \"{name}\" no encontrado")
    repo.delete(name)
    return {"message": f"Alimento \"{name}\" eliminado correctamente"}