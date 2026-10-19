from app.util import read_from_file

def parse_id(title: str):
    from app.repositories.product_repositories import PRODUCTS_IN_SHOP_PATH, str_to_class
    products_str = read_from_file(PRODUCTS_IN_SHOP_PATH)
    for product_str in products_str:
        product = str_to_class(product_str)
        if product.title == title:
            return product.id
    raise ValueError