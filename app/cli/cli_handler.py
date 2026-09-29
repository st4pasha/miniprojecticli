import app.services.shop_services as shop

def get_products():
    products = shop.get_products()
    print("Доступные товары: ")
    for i in range(len(products)):
        print(f"{i + 1}: {products[i]["title"]}, цена: {products[i]["price"]}")


def get_products_from_basket():
    basket = shop.get_products_from_basket()
    print("Товары в корзине: ")
    for product in basket:
        print(f"Название: {product.title}, цена {product.price}")

def get_orders():
    orders = shop.get_orders()
    print("Список заказов: ")
    for order in orders:
        print(f"Название товара: {order.title}, цена: {order.price}, ID: {order.id}")