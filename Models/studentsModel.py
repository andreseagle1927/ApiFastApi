# Importa las clases Column, Integer, String y DateTime de SQLAlchemy.
from sqlalchemy import Column, Integer, String, DateTime

# Importa la clase declarative_base de SQLAlchemy, que se utiliza para definir modelos de datos.
from sqlalchemy.orm import declarative_base

# Crea una instancia de la clase declarative_base y la almacena en la variable Base.
Base = declarative_base()

# Define la clase StudentModel, que hereda de la clase Base, lo que significa que se trata de un modelo de datos SQLAlchemy.
class StudentModel(Base):
    # Define el nombre de la tabla en la base de datos a la que se mapeará este modelo.
    __tablename__ = "Students"

    # Define las columnas de la tabla Students y sus propiedades.
    # Id es una columna de tipo Integer, que servirá como clave primaria (primary_key=True) e índice (index=True).
    Id = Column(Integer, primary_key=True, index=True)

    # FirstName es una columna de tipo String con un límite máximo de 50 caracteres (String(50)),
    # y no se permite que sea nulo en la base de datos (nullable=False).
    FirstName = Column(String(50), nullable=False)

    # LastName es una columna de tipo String con un límite máximo de 50 caracteres (String(50)),
    # pero se permite que sea nulo en la base de datos.
    LastName = Column(String(50))

    # DateOfBirth es una columna de tipo DateTime, y no se permite que sea nulo en la base de datos (nullable=False).
    DateOfBirth = Column(DateTime, nullable=False)

    # Sex es una columna de tipo String con un límite máximo de 1 carácter (String(1)),
    # y no se permite que sea nulo en la base de datos (nullable=False).
    Sex = Column(String(1), nullable=False)

# Define una clase Config que tiene un atributo llamado orm_mode que se establece en True.
# Este atributo se usa para habilitar el modo ORM (Object-Relational Mapping) al trabajar con este modelo.
class Config:
    orm_mode = True
