from app.models.order_class import Order
import sqlite3

order_connection = sqlite3.connect("app/data/orders.db")
cursor_order = order_connection.cursor()
order_connection.execute("CREATE TABLE IF NOt EXISTS orders(id TEXT, product_id TEXT UNIQUE)")

def order_to_str(order: Order):
    lst = []

    lst.append(order.id)
    lst.append(order.title)
    lst.append(str(order.price))

    return "|".join(lst)

def str_to_class(order_str: str):
    orders_str = order_str.split("|")
    
    id = orders_str[0]
    title = orders_str[1]
    price = orders_str[2]

    return Order(id, title, float(price))