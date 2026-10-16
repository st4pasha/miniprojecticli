from app.util import read_from_file, write_to_file
from app.models.product_class import Product

products = [
    {"title": "молоко", "price": 100}, 
    {"title": "чипсы", "price": 80}, 
    {"title": "хлеб", "price": 50}
    ]

BASKET_FILE_PATH = "app/data/basket.csv"

def get_products_from_repositories():
    return products

def create_product(title: str, price = float):
    return Product(title, price)

def product_to_str(product: Product) -> str:
    lst = [] # ['Хлеб', '50']

    lst.append(product.title)
    lst.append(str(product.price))

    return "|".join(lst)

def write_product_to_file(product: Product):

    with open(BASKET_FILE_PATH, "w") as file:
        file.write(product_to_str(product) + "\n")



def str_to_class(product_str: str):
    product_list = product_str.split("|")

    title = product_list[0]
    price = float(product_list[1])

    return Product(title, price)

def read_products_from_file():
    products: list[Product] = []
    products_str = read_from_file(BASKET_FILE_PATH)
    
    for product_str in products_str:
        product = str_to_class(product_str.strip())
        products.append(product)


    return products