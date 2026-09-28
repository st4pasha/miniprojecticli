from app.repositories.product_repositories import get_products_from_repositories, products
from app.repositories.basket_repositories import basket, get_products_from_basket_from_repositories
from app.repositories.order_repositories import orders, get_orders_from_repositories
from app.models.product_class import Product
from app.models.order_class import Order
from uuid import uuid4

def get_products():
    return get_products_from_repositories()

def add_to_basket(title: str):
    for product_item in products:
        if product_item["title"] == title:
            product_to_basket = Product(title=product_item["title"], price=float(product_item["price"]))
            basket.append(product_to_basket)
            return f"Товар: {title} добавлен в корзину."
    return f"Товар с названием {title} в магазине не найден."

def get_products_from_basket():
    return get_products_from_basket_from_repositories()

def do_order(title: str):
    for product in basket:
        if product.title == title:
            product_to_order = Order(id=str(uuid4()), title=product.title, price=product.price)
            orders.append(product_to_order)

            basket.remove(product)
            return f"Оформлен заказ продукта: {product_to_order.title}"

    return f"Товар с названием {title} в корзине не найден"

def get_orders():
    return get_orders_from_repositories()