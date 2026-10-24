from app.repositories.product_repositories import get_products_from_repositories, read_products_from_basket, read_products_from_orders
from app.repositories.order_repositories import add_product_to_orders
from app.repositories.basket_repositories import add_product_to_basket

def get_products():
    return get_products_from_repositories()

def add_to_basket(id: str):
    if add_product_to_basket(id):
        return f"Продукт с айди: {id} успешно добавлен в корзину"
    return f"Продукта с айди: {id} нет в магазине"


def get_products_from_basket():
    return read_products_from_basket()

def do_order(id: str):
    if add_product_to_orders(id):
        return f"Продукт с айди: {id} успешно заказан"
    return f"Продукта с айди: {id} нет в корзине"

def get_orders():
    return read_products_from_orders()