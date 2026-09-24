from app.models.product import products
from app.models.basket import basket
from app.models.order import orders

def get_products():
    print("Доступные товары: ")
    for i in range(len(products)):
        print(f"{i + 1}: {products[i]["title"]}, цена: {products[i]["price"]}")

def add_to_basket(title: str):
    for product in products:
        if product["title"] == title:
            basket.append(product)
            return f"Товар: {title} добавлен в корзину."
    return f"Товар с названием {title} в магазине не найден."

def get_products_from_basket():
    print("Товары в корзине: ")
    for product in basket:
        print(f"Название: {product["title"]}, цена {product["price"]}")

def do_order(title: str):
    for product in basket:
        if product["title"] == title:
            orders.append(product)
            basket.remove(product)
            return f"Оформлен заказ продукта: {product["title"]}"

    return f"Товар с названием {title} в корзине не найден"

def get_orders():
    print("Список заказов: ")
    for order in orders:
        print(f"Название товара: {order["title"]}, цена: {order["price"]}.")