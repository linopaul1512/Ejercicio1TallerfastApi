from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import asyncio
from sqlalchemy.orm import declarative_base
# Configuración de SQLAlchemy
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

# Crear el engine y la base de datos
engine = create_engine('sqlite:///items.db')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una nueva sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos de ejemplo para la tabla items
items_data = [
    {'name': 'Item 1', 'description': 'Hola'},
    {'name': 'Item 2', 'description': 'Mundo'},
    {'name': 'Item 3', 'description': 'Sol'},
    {'name': 'Item 4', 'description': 'Mercurio'},
    {'name': 'Item 5', 'description': 'Venus'},
    {'name': 'Item 6', 'description': 'Tierra'},
    {'name': 'Item 7', 'description': 'Marte'},
    {'name': 'Item 8', 'description': 'Jupiter'},
    {'name': 'Item 9', 'description': 'Saturno'},
    {'name': 'Item 10', 'description': 'Urano'}
]

# Añadir los datos a la sesión y guardar los cambios
for data in items_data:
    item = Item(name=data['name'], description=data['description'])
    session.add(item)

session.commit()

# Función para consultar items de forma asíncrona
async def read_items():
    print("Loading... Buscando items ingresados en la base de datos...")
    await asyncio.sleep(2)  # Simular un tiempo de espera para la consulta
    items = session.query(Item).all()
    print("Items encontrados:")
    for item in items:
        print(f"Nombre: {item.name}, Descripción: {item.description}")

async def main():
    await read_items()

# Ejecutar la función principal de forma asíncrona
asyncio.run(main())
