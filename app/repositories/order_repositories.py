from app.models.order_class import Order

orders: list[Order] = []

def get_orders_from_repositories():
    return orders