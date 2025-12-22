from sqlalchemy import Column, Integer, String, Float
from infrastructure.database import Base

class FoodEntity(Base):
    __tablename__ = "foods"

    id = Column(Integer,primary_key=True, index=True)
    name= Column(String,index=True)

    protein_per_100g = Column(Float)
    carbs_per_100g = Column(Float)
    fats_per_100g = Column(Float)