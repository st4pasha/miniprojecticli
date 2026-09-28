from app.models.product_class import Product

basket: list[Product] = []

def get_products_from_basket_from_repositories():
    return basket