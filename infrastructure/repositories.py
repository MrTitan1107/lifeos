from typing import List, Optional
from domain.models import Food
import os
import csv
class CSVRepository:
    def __init__(self, file_path: str):
        # Aquí guardaremos la ruta del archivo (ej: "data/foods.csv")
        self.file_path = file_path

        self.fieldnames = ["name","protein_per_100g","carbs_per_100g","fats_per_100g"]

        if not os.path.exists(file_path):
            try:
                with open (file_path, "w") as f:
                    f.write("name,protein_per_100g,carbs_per_100g,fats_per_100g\n")
            except Exception as e:
                print(f"Could not create file at {file_path}: {e}")

    
    def get_all(self) -> List[Food]:
        """Devuelve TODOS los alimentos del CSV convertidos en objetos Food."""
        foods = []
        if not os.path.exists(self.file_path):
            return []
        
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    foods.append(Food(
                        name=row["name"],
                        protein_per_100g=float(row["protein_per_100g"]),
                        carbs_per_100g=float(row["carbs_per_100g"]),
                        fats_per_100g=float(row["fats_per_100g"])
                    ))
                except:
                    continue
        return foods

    def save(self, food: Food) -> None:
        if not os.path.exists(self.file_path):
            return False
        foods = self.get_all()

        updated_foods = [f for f in foods if f.name() != food.name]

        updated_foods.append(food)

        with open(self.file_path, "w") as f:

            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for f_item in updated_foods:
                writer.writerow(
                    {
                        "name": food.name,
                        "protein_per_100g": food.protein_per_100g,
                        "carbs_per_100g": food.carbs_per_100g,
                        "fats_per_100g": food.fats_per_100g
                    }
                )








    def find_by_name(self, name: str) -> Optional[Food]:
        """Busca uno específico. Devuelve None si no existe."""
        pass
        
    def delete(self, name: str) -> None:
        """Elimina el alimento del archivo."""
        pass