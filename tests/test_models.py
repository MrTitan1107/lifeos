import pytest
from domain.models import Food

# ---------------------------------------------------------
# CASO 1: THE HAPPY PATH (Todo sale bien)
# ---------------------------------------------------------
def test_food_creation_success():
    """Verifica que un alimento válido se crea y calcula bien."""
    # 1. ARRANGE (Preparamos ingredientes)
    name = "Pechuga de Pollo"
    prot = 23.0
    carb = 0.0
    fat = 1.0
    
    # 2. ACT (Cocinamos/Ejecutamos)
    chicken = Food(name=name, protein_per_100g=prot, carbs_per_100g=carb, fats_per_100g=fat)
    
    # 3. ASSERT (Probamos/Validamos)
    assert chicken.name == "Pechuga de Pollo"
    
    # Cálculo esperado: (23 * 4) + (0 * 4) + (1 * 9) = 92 + 9 = 101 kcal
    # Usamos math.isclose si fueran floats complejos, pero aquí es simple.
    assert chicken.calories_per_100g == 101.0

# ---------------------------------------------------------
# CASO 2: THE SAD PATH (Intentamos romperlo)
# ---------------------------------------------------------
def test_food_creation_invalid_negative_values():
    """Verifica que NO se permitan valores negativos (Defensive Design)."""
    
    # pytest.raises actúa como un "cazador de errores".
    # Dice: "Espero que el siguiente código falle con un ValueError. Si NO falla, el test fracasa".
    with pytest.raises(ValueError):
        Food(name="Manzana Imposible", protein_per_100g=-10, carbs_per_100g=0, fats_per_100g=0)

# ---------------------------------------------------------
# CASO 3: LOGIC CHECK (Cálculo con peso)
# ---------------------------------------------------------
def test_calculate_calories_specific_weight():
    """Verifica la regla de tres para pesos distintos a 100g."""
    # Arroz: 80g carb, 2g prot, 0g fat = (320 + 8) = 328 kcal por 100g
    rice = Food(name="Arroz", protein_per_100g=2, carbs_per_100g=80, fats_per_100g=0)
    
    # Si como 200g, debo tener el doble de calorías
    cals = rice.calculate_calories(200)
    assert cals == 656.0
    
    # Si como 50g, debo tener la mitad
    cals_half = rice.calculate_calories(50)
    assert cals_half == 164.0