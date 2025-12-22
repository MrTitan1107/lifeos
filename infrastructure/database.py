from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Definimos el nombre del archivo de la base de datos
# "sqlite:///" indica que usaremos SQLite (base de datos en un archivo)
DATABASE_URL = "sqlite:///./lifeos.db"

# 2. Creamos el "Motor" (Engine)
# check_same_thread=False es necesario solo para SQLite en FastAPI
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Creamos la "Fábrica de Sesiones" (SessionLocal)
# Cada vez que alguien pida algo a la API, usaremos esto para abrir una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos la "Clase Base"
# Todos nuestros modelos de datos heredarán de aquí para que SQLAlchemy sepa que son tablas
Base = declarative_base()

