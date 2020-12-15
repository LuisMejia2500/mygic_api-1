from pydantic import BaseModel
from datetime import date

class ProductIn(BaseModel):
    codigo: str
    nombre: str    

class ProductCreate(BaseModel):
    codigo: str
    nombre: str
    cantidad_disponible: int
    costo_adquisicion: float
    precio_venta: float
    #fecha_caducidad: date

class ProductOut(BaseModel):    
    nombre: str
    cantidad_disponible: int
    costo_adquisicion: float
    precio_venta: float
    #fecha_caducidad: date
    
    