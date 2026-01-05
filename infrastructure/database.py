from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os # <--- Importante para leer variables de entorno

# 1. Buscamos la dirección de la BD en las variables de entorno
# Si no existe (estamos en local), usamos SQLite por defecto.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./lifeos.db")

# 2. CORRECCIÓN IMPORTANTE PARA RENDER
# Render nos da la URL empezando por "postgres://", pero SQLAlchemy
# necesita que empiece por "postgresql://". Hacemos el cambio manual:
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Configuración del motor según el tipo de BD
if "sqlite" in DATABASE_URL:
    # Configuración para SQLite (lo que tenías antes)
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # Configuración para PostgreSQL (La Nube)
    # PostgreSQL es más robusto y no necesita check_same_thread
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
