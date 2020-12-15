from db.products_db import ProductsInDB
from db.products_db import save_product, get_product, delete_product

from models.product_models import ProductIn, ProductOut, ProductCreate

from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/product/")
async def create_product(product_create: ProductCreate):
    #Totas las comprobaciones Necesarias
    product_create = get_product(product_create.codigo)

    if product_create != None:        
        raise HTTPException(status_code= 400, detail= "El producto ya existe")
    
    product_saved = save_product(ProductsInDB(**product_create.dict()))
    return ProductOut(**product_saved.dict())



@api.get("/product/{codigo}")
async def get_balance(codigo: str):

    product_in_db = get_product(codigo)

    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    product_out = ProductOut(**product_in_db.dict())

    return product_out