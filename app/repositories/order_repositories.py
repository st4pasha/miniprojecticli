from app.models.order_class import Order
from uuid import uuid4
from app.repositories.product_repositories import get_products_from_repositories
import sqlite3

order_connection = sqlite3.connect("app/data/orders.db")
cursor_order = order_connection.cursor()
order_connection.execute("CREATE TABLE IF NOt EXISTS orders(id TEXT, product_id TEXT UNIQUE)")

def add_product_to_orders(product_id: str):

    products = get_products_from_repositories()
    for product in products:
        if product.id == product_id:
            order_connection.execute("INSERT INTO orders(id, product_id) VALUES(?, ?)", (str(uuid4()), product_id))
            order_connection.commit()
            return True
    return False

def order_to_str(order: Order):
    lst = []

    lst.append(order.id)
    lst.append(order.title)
    lst.append(str(order.price))

    return "|".join(lst)

def str_to_class(order_str: str):
    orders_str = order_str.split("|")
    
    id = orders_str[0]
    title = orders_str[1]
    price = orders_str[2]

    return Order(id, title, float(price))