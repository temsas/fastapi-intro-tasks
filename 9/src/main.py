from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)
    specifications: ProductSpecifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: ProductSpecifications

@app.post("/product")
async def create_product(product: Product):
    global product_id_counter, product_list
    product_data = product.dict()
    product_data['id'] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return product_data

@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    return [{"id": product["id"], "name": product["name"], "price": product["price"]} for product in product_list]

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
def get_product(product_id: int):
    product = next((p for p in product_list if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# END