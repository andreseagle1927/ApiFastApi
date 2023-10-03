import os  # Importa el módulo os para trabajar con variables de entorno y el sistema de archivos.
from sqlalchemy import create_engine, MetaData  # Importa clases de SQLAlchemy para manejar la base de datos.
from sqlalchemy.orm import declarative_base, sessionmaker  # Importa clases de SQLAlchemy para ORM.
from databases import Database  # Importa la clase Database de la biblioteca Databases.
from dotenv import load_dotenv  # Importa la función load_dotenv para cargar variables de entorno desde un archivo .env.

# Carga las variables de entorno desde un archivo .env si existe.
load_dotenv()

# Obtiene la URL de la base de datos desde una variable de entorno llamada "DATABASE_URL".
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea una instancia de la clase Database de Databases para representar la base de datos.
database = Database(DATABASE_URL)
metadata = MetaData()  # Crea una instancia de la clase MetaData de SQLAlchemy.

# Crea un motor SQLAlchemy que establece la conexión a la base de datos utilizando la URL de la base de datos.
engine = create_engine(DATABASE_URL)

# Crea una fábrica de sesiones SQLAlchemy (sessionmaker) que se utilizará para crear sesiones de base de datos.
# "autocommit=False" y "autoflush=False" se configuran para controlar manualmente las transacciones y la escritura en la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase Base de SQLAlchemy (declarative_base) que se utilizará para definir modelos de base de datos utilizando el ORM de SQLAlchemy.
Base = declarative_base()
