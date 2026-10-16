from app.models.order_class import Order
from app.repositories.product_repositories import *
from app.util import *

orders: list[Order] = []

ORDER_FILE_PATH = "app/data/order.csv"

def get_orders_from_repositories():
    return orders

def create_order(id: str, title: str, price: float):
    return Order(id, title, price)

def order_to_str(order: Order):
    lst = []

    lst.append(order.id)
    lst.append(order.title)
    lst.append(str(order.price))

    return "|".join(lst)

def write_order_to_file(order: Order):
    with open(ORDER_FILE_PATH, "w") as file:
        file.write(order_to_str(order) + "\n")

def str_to_class(order_str: str):
    orders_str = order_str.split("|")
    
    id = orders_str[0]
    title = orders_str[1]
    price = orders_str[2]

    return Order(id, title, float(price))
    
def read_order_from_file():

    orders: list[Order] = []

    orders_str = read_from_file(ORDER_FILE_PATH)

    for order_str in orders_str:
        order = str_to_class(order_str.strip())
        orders.append(order)
        return orders