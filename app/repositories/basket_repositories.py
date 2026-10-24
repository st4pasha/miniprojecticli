from app.util import write_to_file
from uuid import uuid4
from app.util import colons

def add_product_to_basket(product_id: str):
    from app.repositories.product_repositories import get_products_from_repositories, BASKET_FILE_PATH

    products = get_products_from_repositories()

    for product in products:
        if product.id == product_id:
            str_to_file = f"{str(uuid4())}|{product_id}"
            write_to_file(BASKET_FILE_PATH, (colons + str_to_file))
            return True
    return False
