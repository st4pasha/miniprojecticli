from app.util import read_from_file, parse_id
from app.models.product_class import Product
from app.models.order_class import Order

ORDER_FILE_PATH = "app/data/order.csv"
BASKET_FILE_PATH = "app/data/basket.csv"
PRODUCTS_IN_SHOP_PATH = "app/data/products_in_shop.csv"
colons = "id|product_id\n"

def get_products_from_repositories():

    products: list[Product] = []
    products_str = read_from_file(PRODUCTS_IN_SHOP_PATH)[1::]
        
    for product_str in products_str:
        product = str_to_class(product_str.strip())
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
    products: list[Product] = []

    id = get_product_id_from_file(BASKET_FILE_PATH)

    products_from_file = get_products_from_repositories()
    for product in products_from_file:
        if product.id == id:
            products.append(product)
    return products

def read_products_from_orders():
    products: list[Order] = []

    id  = get_product_id_from_file(ORDER_FILE_PATH)
    products_from_file = get_products_from_repositories()
    for product in products_from_file:
        if product.id == id:
            products.append(product)
    return products

def get_product_id_from_file(parse: str):

    ids = read_from_file(parse)[1::]
    id = "|".join(ids)

    return parse_id(id)