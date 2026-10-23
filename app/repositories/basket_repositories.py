from app.util import read_from_file, write_to_file
from uuid import uuid4

def write_id_to_basket(id: str):
    from app.repositories.product_repositories import get_products_from_repositories, BASKET_FILE_PATH

    products = get_products_from_repositories()

    for product in products:
        if product.id == id:
            str_to_file = f"{str(uuid4())}|{id}"
            write_to_file(BASKET_FILE_PATH, str_to_file)
            return True
    return False

def parse_id(id: str):
    ids = id.split("|")
    return ids[1].strip()

def get_id_from_basket():
    from app.repositories.product_repositories import BASKET_FILE_PATH

    ids = read_from_file(BASKET_FILE_PATH)
    id = "|".join(ids)

    return parse_id(id)