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
        print(f"ID: {product.id}: Название: {product.title}, цена {product.price}")

def get_orders():
    orders = shop.get_orders()
    print("Список заказов: ")
    if orders != None:
        for order in orders:
            print(f"ID: {order.id}, название товара: {order.title}, цена: {order.price}.")
    else:
        print("Список заказов пуст.")

def add_to_basket():
    product_id = input("Введите айди товара для добавления в корзину: ")
    print(shop.add_to_basket(product_id))


def do_order():
    product_id = input("Введите айди товара из корзины чтобы оформить заказ: ")
    print(shop.do_order(product_id))