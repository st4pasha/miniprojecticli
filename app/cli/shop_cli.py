import app.services.shop_services as shop

print("Добро пожаловать в магазин")
commands = """Список команд:
1.Отобразить список товаров.
2.Добавить товар в корзину.
3.Отобразить содержание корзины.
4.Оформить заказ.
5.Отобразить список заказов.
6.Отобразить список команд.
7.Выход."""

print(commands)

while True:
    option = input("Выберите цифру для действия: ")
    if option == "1":
        products = shop.get_products()
        print("Доступные товары: ")
        for i in range(len(products)):
            print(f"{i + 1}: {products[i]["title"]}, цена: {products[i]["price"]}")
    elif option == "2":
        product_title = input("Введите название товара для добавления в корзину: ")
        print(shop.add_to_basket(product_title))
    elif option == "3":
        basket = shop.get_products_from_basket()
        print("Товары в корзине: ")
        for product in basket:
            print(f"Название: {product.title}, цена {product.price}")

    elif option == "4":
        product_title = input("Введите название товара из корзины чтобы оформить заказ: ")
        print(shop.do_order(product_title))
    elif option == "5":
        orders = shop.get_orders()
        print("Список заказов: ")
        for order in orders:
            print(f"Название товара: {order.title}, цена: {order.price}, ID: {order.id}")
    elif option == "6":
        print(commands)
    elif option == "7":
        print("Совершён выход из магазина.")
        break
    else:
        print("Непонятная задача, попробуйте снова.")