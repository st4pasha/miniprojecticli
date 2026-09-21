import shop

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
        shop.GetProducts()
    elif option == "2":
        productTitle = input("Введите название товара для добавления в корзину: ")
        print(shop.addToBasket(productTitle))
    elif option == "3":
        shop.GetProductFromBasket()
    elif option == "4":
        productTitle = input("Введите название товара из корзины чтобы оформить заказ: ")
        print(shop.DoOrder(productTitle))
    elif option == "5":
        shop.GetOrders()
    elif option == "6":
        print(commands)
    elif option == "7":
        print("Совершён выход из магазина.")
        break
    else:
        print("Непонятная задача, попробуйте снова.")