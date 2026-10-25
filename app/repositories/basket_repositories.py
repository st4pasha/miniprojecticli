from app.util import write_to_file
from uuid import uuid4
from app.repositories.product_repositories import get_products_from_repositories
import sqlite3

basket_connection = sqlite3.connect("app/data/basket.db")
basket_connection.execute("CREATE TABLE IF NOT EXISTS basket(id TEXT, product_id TEXT UNIQUE)")
cursor_basket = basket_connection.cursor()

def add_product_to_basket(product_id: str):
    products = get_products_from_repositories()

    for product in products:
        if product.id == product_id:
            basket_connection.execute("INSERT INTO basket(id, product_id) VALUES (?, ?)", (str(uuid4()), product_id))
            basket_connection.commit()
            return True
        
    return False
