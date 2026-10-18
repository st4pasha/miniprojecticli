import app.services.shop_services as shop

def get_products():
    products = shop.get_products()
    print("Доступные товары: ")
    for product in products:
        print(f"{product.id}: {product.title}, цена: {product.price}")


def get_products_from_basket():
    basket = shop.get_products_from_basket()
    print("Товары в корзине: ")
    for product in basket:
        print(f"Название: {product.title}, цена {product.price}, айди: {product.id}")

def get_orders():
    orders = shop.get_orders()
    print("Список заказов: ")
    if orders != None:
        for order in orders:
            print(f"Название товара: {order.title}, цена: {order.price}, ID: {order.id}")
    else:
        print("Список заказов пуст.")

def add_to_basket():
    product_title = input("Введите название товара для добавления в корзину: ")
    print(shop.add_to_basket(product_title))


def do_order():
    product_title = input("Введите название товара из корзины чтобы оформить заказ: ")
    print(shop.do_order(product_title))