import pytest
from Class import Product, Order, User

# ==== Тести класу Product ====

def test_product_availability_true():
    product = Product(1, "Монітор", 3000.0, 10)
    assert product.is_available(5) is True

def test_product_availability_false():
    product = Product(2, "Монітор", 3000.0, 3)
    assert product.is_available(5) is False

def test_product_availability_default_quantity():
    product = Product(3, "Мишка", 300.0, 1)
    assert product.is_available() is True

# ==== Тести класу Order ====

def test_add_product_success():
    user = User(1, "user1", "user1@example.com", "pass")
    product = Product(1, "Клавіатура", 1000.0, 5)
    order = Order(1, user)
    order.add_product(product)
    assert product in order.products

def test_add_product_out_of_stock():
    user = User(1, "user1", "user1@example.com", "pass")
    product = Product(2, "Камера", 2000.0, 0)
    order = Order(2, user)
    with pytest.raises(ValueError):
        order.add_product(product)

def test_remove_product_success():
    user = User(1, "user1", "user1@example.com", "pass")
    product = Product(3, "Принтер", 1500.0, 3)
    order = Order(3, user)
    order.add_product(product)
    order.remove_product(product)
    assert product not in order.products

def test_order_total_price():
    user = User(1, "user1", "user1@example.com", "pass")
    order = Order(4, user)
    p1 = Product(4, "USB-хаб", 500.0, 10)
    p2 = Product(5, "HDMI кабель", 300.0, 10)
    order.add_product(p1)
    order.add_product(p2)
    assert order.calculate_total() == 800.0

# ==== Тести класу User ====

def test_user_register():
    user = User(1, "testuser", "test@email.com", "password")
    assert user.register() == "User testuser registered successfully."

def test_user_login():
    user = User(2, "tester", "tester@email.com", "1234")
    assert user.login() == "User tester logged in."

def test_user_view_orders_empty():
    user = User(3, "no_orders", "no@email.com", "none")
    assert user.view_orders() == []

# ==== Тест взаємодії між об’єктами ====

def test_user_place_order():
    user = User(4, "shopper", "shopper@email.com", "secure")
    product = Product(6, "Колонка", 1200.0, 2)
    order = Order(5, user)
    order.add_product(product)
    user.place_order(order)
    assert len(user.view_orders()) == 1
    assert user.view_orders()[0].products[0].name == "Колонка"

def test_multiple_orders_and_totals():
    user = User(5, "multi", "multi@email.com", "pw")
    order1 = Order(6, user)
    order2 = Order(7, user)
    p1 = Product(7, "SSD", 3000.0, 5)
    p2 = Product(8, "ОЗП", 1500.0, 5)
    order1.add_product(p1)
    order2.add_product(p2)
    user.place_order(order1)
    user.place_order(order2)
    assert user.view_orders()[0].calculate_total() == 3000.0
    assert user.view_orders()[1].calculate_total() == 1500.0

# ==== Крайній випадок ====

def test_remove_nonexistent_product():
    user = User(6, "ghost", "ghost@email.com", "invis")
    product1 = Product(9, "Мікрофон", 900.0, 2)
    product2 = Product(10, "Навушники", 1100.0, 2)
    order = Order(8, user)
    order.add_product(product1)
    order.remove_product(product2)  # Не було в замовленні
    assert product1 in order.products  # Перевірка, що нічого не зіпсувалось
