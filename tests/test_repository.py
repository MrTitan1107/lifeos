import os
import pytest
from domain.models import Food
from infrastructure.repositories import CSVRepository

# Fixture: Esto se ejecuta ANTES de cada test para preparar el terreno
@pytest.fixture
def repo():
    test_file = "test_foods.csv"
    # Setup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    repository = CSVRepository(test_file)
    yield repository # Aquí corre el test
    
    # Teardown (Limpieza después del test)
    if os.path.exists(test_file):
        os.remove(test_file)

def test_save_and_retrieve_food(repo):
    # 1. Crear alimento
    apple = Food(name="Manzana", protein_per_100g=0.3, carbs_per_100g=14, fats_per_100g=0.2)
    
    # 2. Guardar
    repo.save(apple)
    
    # 3. Recuperar todo
    all_foods = repo.get_all()
    
    # 4. Verificar
    assert len(all_foods) == 1
    assert all_foods[0].name == "Manzana"
    assert all_foods[0].carbs_per_100g == 14.0

def test_persistence(repo):
    """Verifica que si cerramos el repo y lo abrimos, los datos siguen ahí."""
    pizza = Food(name="Pizza", protein_per_100g=10, carbs_per_100g=30, fats_per_100g=10)
    repo.save(pizza)
    
    # Creamos UNA NUEVA instancia del repo apuntando al mismo archivo
    repo_v2 = CSVRepository(repo.file_path)
    loaded_foods = repo_v2.get_all()
    
    assert len(loaded_foods) == 1
    assert loaded_foods[0].name == "Pizza"