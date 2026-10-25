from fastapi import FastAPI
from app.services.shop_services import *

app = FastAPI()

@app.get("/products")
def get_products_from_shop():
    return get_products()

@app.post("/products/{id}")
def add_products_to_basket(id: str):
    return add_to_basket(id)

@app.get("/baskets")
def get_products_from_bucket():
     return get_products_from_basket()

@app.post("/orders/{id}")
def add_product_to_order(id: str):
    return do_order(id)

@app.get("/orders")
def get_products_from_orders():
    return get_orders()

