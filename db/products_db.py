from typing import Dict
from pydantic import BaseModel
from datetime import date

class ProductsInDB(BaseModel):
    codigo: str
    nombre: str
    cantidad_disponible: int
    costo_adquisicion: float
    precio_venta: float
    #fecha_caducidad: date    

#Base de datos en diccionario
database_products = Dict[str, ProductsInDB]

database_products ={ }

def save_product(product_in_db: ProductsInDB):
    database_products[product_in_db.codigo] = product_in_db
    return product_in_db

def get_product(codigo_producto: str):
    if codigo_producto in database_products.keys():
        return database_products[codigo_producto]
    else:
        return None

def delete_product(codigo_producto:str):
    if codigo_producto in database_products.keys():
        product_delete = database_products[codigo_producto]
        del database_products[codigo_producto]
        return product_delete        
    else:
        return None