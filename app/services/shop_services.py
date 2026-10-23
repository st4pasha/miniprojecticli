from app.repositories.product_repositories import get_products_from_repositories, read_products_from_basket
from app.repositories.order_repositories import create_order, ORDER_FILE_PATH, order_to_str, read_order_from_file
from app.repositories.basket_repositories import write_id_to_basket
from app.util import write_to_file

def get_products():
    return get_products_from_repositories()

def add_to_basket(id: str):
    if write_id_to_basket(id):
        return f"Продукт с айди: {id} успешно добавлен в корзину"
    return f"Продукта с айди: {id} нет в магазине"


def get_products_from_basket():
    return read_products_from_basket()

def do_order(id: str):

    basket = read_products_from_basket()

    for product in basket:
        if product.id == id:
            order = create_order(title=product.title, price=product.price)
            write_to_file(ORDER_FILE_PATH, order_to_str(order))
            return f"Товар {product.title} добавлен в список заказов"
    return f"Товар с названием {product.title} в корзине не найден"

def get_orders():
    return read_order_from_file()