from app.util import read_from_file, write_to_file
from app.models.product_class import Product
from uuid import uuid4
from app.repositories.basket_repositories import parse_id

BASKET_FILE_PATH = "app/data/basket.csv"
PRODUCTS_IN_SHOP_PATH = "app/data/products_in_shop.csv"

def get_products_from_repositories():

    products: list[Product] = []
    products_str = read_from_file(PRODUCTS_IN_SHOP_PATH)
        
    for product_str in products_str:
        product = str_to_class(product_str.strip())
        products.append(product)
    return products

def create_product(title: str, price: float):
    return Product(parse_id(title), title, price)

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

def read_products_from_file():
    products: list[Product] = []
    products_str = read_from_file(BASKET_FILE_PATH)
    
    for product_str in products_str:
        product = str_to_class(product_str.strip())
        products.append(product)


    return products