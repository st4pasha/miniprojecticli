Products = [
    {"title": "молоко", "price": 100}, 
    {"title": "чипсы", "price": 80}, 
    {"title": "хлеб", "price": 50}
    ]

basket = []
orders = []

def GetProducts():
    print("Доступные товары: ")
    for i in range(len(Products)):
        print(f"{i + 1}: {Products[i]["title"]}, цена: {Products[i]["price"]}")

def addToBasket(title: str):
    for product in Products:
        if product["title"] == title:
            basket.append(product)
            return f"Товар: {title} добавлен в корзину."
    return f"Товар с названием {title} в магазине не найден."

def GetProductFromBasket():
    print("Товары в корзине: ")
    for product in basket:
        print(f"Название: {product["title"]}, цена {product["price"]}")

def DoOrder(title: str):
    for product in basket:
        if product["title"] == title:
            orders.append(product)
            basket.remove(product)
            return f"Оформлен заказ продукта: {product["title"]}"

    return f"Товар с названием {title} в корзине не найден"

def GetOrders():
    print("Список заказов: ")
    for order in orders:
        print(f"Название товара: {order["title"]}, цена: {order["price"]}.")