import app.services.shop_services as shop
from app.cli import cli_handler as cli
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
        cli.get_products()
    elif option == "2":
        cli.add_to_basket()
    elif option == "3":
        cli.get_products_from_basket()
    elif option == "4":
        cli.do_order()
    elif option == "5":
        cli.get_orders()
    elif option == "6":
        print(commands)
    elif option == "7":
        print("Совершён выход из магазина.")
        break
    else:
        print("Непонятная задача, попробуйте снова.")