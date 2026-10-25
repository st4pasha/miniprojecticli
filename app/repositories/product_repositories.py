from app.util import parse_id
from app.models.product_class import Product
import sqlite3

ORDER_FILE_PATH = "app/data/order.csv"
BASKET_FILE_PATH = "app/data/basket.csv"
PRODUCTS_IN_SHOP_PATH = "app/data/products_in_shop.csv"
colons = "id|product_id\n"

product_connection = sqlite3.connect("app/data/product_in_shop.db")
product_connection.execute("CREATE TABLE IF NOT EXISTS products_in_shop(id INT UNIQUE, title TEXT UNIQUE, price FLOAT)")
cursor_product = product_connection.cursor()

def get_products_from_repositories():

    cursor_product.execute("SELECT * FROM products_in_shop")
    products_tuple = cursor_product.fetchall()

    products: list[Product] = []

    for product_tuple in products_tuple:

        product_lst = (list(product_tuple))
        
        id = product_lst[0]
        title = product_tuple[1]
        price = product_tuple[2]

        product = str_to_class(f"{id}|{title}|{price}")
        products.append(product)

    return products
  
def product_to_str(product: Product) -> str:
    lst = [] # ['Хлеб', '50']

    lst.append(product.id)
    lst.append(product.title)
    lst.append(str(product.price))

    return "|".join(lst)


def str_to_class(product_str: str):
    product_list = product_str.split("|")

    id = product_list[0]
    title = product_list[1]
    price = float(product_list[2])

    return Product(id, title, price)

def read_products_from_basket():
    from app.repositories.basket_repositories import cursor_basket
    products: list[Product] = []

    cursor_basket.execute("SELECT * FROM basket")

    ids_tuple = cursor_basket.fetchall()
    id = parse_id(list(ids_tuple[0]))

    products_from_file = get_products_from_repositories()

    for product in products_from_file:
        if product.id == id:
            products.append(product)
    return products

def read_products_from_orders():
    from app.repositories.order_repositories import cursor_order
    products: list[Product] = []
    
    cursor_order.execute("SELECT * FROM orders")
    
    ids_tuple = cursor_order.fetchall()
    id = parse_id(list(ids_tuple[0]))
    
    products_from_file = get_products_from_repositories()
    
    for product in products_from_file:
        if product.id == id:
            products.append(product)
    return products

