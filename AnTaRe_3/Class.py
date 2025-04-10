from typing import List

class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity: int = 1) -> bool:
        return self.stock >= quantity


class Order:
    def __init__(self, order_id: int, user: 'User'):
        self.order_id = order_id
        self.user = user
        self.products: List[Product] = []
        self.status = "Pending"

    def add_product(self, product: Product):
        if product.is_available():
            self.products.append(product)
        else:
            raise ValueError("Product is out of stock")

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self) -> float:
        return sum(product.price for product in self.products)


class User:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.orders: List[Order] = []

    def register(self):
        return f"User {self.username} registered successfully."

    def login(self):
        return f"User {self.username} logged in."

    def view_orders(self) -> List[Order]:
        return self.orders

    def place_order(self, order: Order):
        self.orders.append(order)
