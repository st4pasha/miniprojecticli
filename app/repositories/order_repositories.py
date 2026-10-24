from app.models.order_class import Order
from app.util import colons, write_to_file
from uuid import uuid4
from app.repositories.product_repositories import get_products_from_repositories, ORDER_FILE_PATH


def add_product_to_orders(product_id: str):
    products = get_products_from_repositories()
    for product in products:
        if product.id == product_id:
            str_to_file = f"{str(uuid4())}|{product_id}"
            write_to_file(ORDER_FILE_PATH, (colons + str_to_file))
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