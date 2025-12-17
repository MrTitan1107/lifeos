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
        
        with open(self.file_path, "r", encoding="utf-8") as f:
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

        updated_foods = [f for f in foods if f.name != food.name]

        updated_foods.append(food)

        with open(self.file_path, "w", newline='', encoding='utf-8') as f:

            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for f_item in updated_foods:
                writer.writerow(
                    {
                        "name": f_item.name,
                        "protein_per_100g": f_item.protein_per_100g,
                        "carbs_per_100g": f_item.carbs_per_100g,
                        "fats_per_100g": f_item.fats_per_100g
                    }
                )

    def find_by_name(self, name: str) -> Optional[Food]:
        """Busca uno específico. Devuelve None si no existe."""
        foods = self.get_all()
        for food in foods:
            if food.name.lower() == name.lower():
                return food
        return None
            
    def delete(self, name: str) -> None:
        """Elimina el alimento del archivo."""
        foods = self.get_all()
        updated_foods = [f for f in foods if f.name != name]
        try:
            with open(self.file_path, "w", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for f_item in updated_foods:
                    writer.writerow(
                        {
                            "name": f_item.name,
                            "protein_per_100g": f_item.protein_per_100g,
                            "carbs_per_100g": f_item.carbs_per_100g,
                            "fats_per_100g": f_item.fats_per_100g
                        }
                    )
        except Exception as e:
            print(f"Could not delete food {name}: {e}")