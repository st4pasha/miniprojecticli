from app.repositories.product_repositories import get_products_from_repositories
from uuid import uuid4
from app.repositories.product_repositories import *
from app.repositories.order_repositories import *
from app.util import write_to_file

def get_products():
    return get_products_from_repositories()

def add_to_basket(id: str):
    for product_item in get_products():
        if product_item.id == id:

            product_title = product_item.title
            product_price = product_item.price

            product = create_product(title=product_title, price=float(product_price))
            write_to_file(BASKET_FILE_PATH, product_to_str(product))
            
            return f"Товар: {product_item.title} добавлен в корзину."
        
    return f"Товар с названием {product_item.title} в магазине не найден."



def get_products_from_basket():
    return read_products_from_file()

def do_order(id: str):

    basket = read_products_from_file()

    for product in basket:
        if product.id == id:
            order = create_order(title=product.title, price=product.price)
            write_to_file(ORDER_FILE_PATH, order_to_str(order))
            return f"Товар {product.title} добавлен в список заказов"
    return f"Товар с названием {product.title} в корзине не найден"

def get_orders():
    return read_order_from_file()