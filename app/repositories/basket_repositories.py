import sqlite3

basket_connection = sqlite3.connect("app/data/basket.db")
basket_connection.execute("CREATE TABLE IF NOT EXISTS basket(id TEXT, product_id TEXT UNIQUE)")
cursor_basket = basket_connection.cursor()

