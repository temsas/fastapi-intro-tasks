from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


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
    specifications : ProductSpecifications

@app.post("/product")
async def add_product(product: Product):
    global product_id_counter
    product_data = product.dict()
    product_data['id'] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return {"message": "Product added successfully", "product": product_data}

@app.get("/products")
async def func():
    return{"products": product_list}
# END
