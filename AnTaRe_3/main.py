from typing import List
from Class import Product, Order, User

products = [
    Product(1, "Ноутбук", 25000, 5),
    Product(2, "Мишка", 500, 10),
    Product(3, "Клавіатура", 1500, 7),
]

users: List[User] = []
logged_user = None
order_counter = 1

def print_products():
    print("\nСписок товарів:")
    for p in products:
        print(f"{p.product_id}. {p.name} — {p.price} грн (в наявності: {p.stock})")

def main():
    global logged_user, order_counter
    print("=== Інтернет-магазин ===")
    while True:
        print("\n[1] Зареєструватися")
        print("[2] Увійти")
        print("[3] Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            uid = len(users) + 1
            username = input("Ім'я користувача: ")
            email = input("Email: ")
            password = input("Пароль: ")
            user = User(uid, username, email, password)
            users.append(user)
            print(user.register())

        elif choice == "2":
            username = input("Ім'я користувача: ")
            password = input("Пароль: ")
            user = next((u for u in users if u.username == username and u.password == password), None)
            if user:
                logged_user = user
                print(user.login())
                user_menu()
            else:
                print("Невірне ім'я користувача або пароль.")

        elif choice == "3":
            print("До зустрічі!")
            break
        else:
            print("Невірний вибір.")

def user_menu():
    global logged_user, order_counter
    current_order = Order(order_counter, logged_user)
    while True:
        print("\n[1] Переглянути товари")
        print("[2] Додати товар")
        print("[3] Видалити товар")
        print("[4] Оформити замовлення")
        print("[5] Переглянути мої замовлення")
        print("[0] Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            print_products()

        elif choice == "2":
            print_products()
            try:
                pid = int(input("Введіть ID товару: "))
                product = next((p for p in products if p.product_id == pid), None)
                if product:
                    current_order.add_product(product)
                    print(f"Додано: {product.name}")
                else:
                    print("Товар не знайдено.")
            except Exception as e:
                print("Помилка:", e)

        elif choice == "3":
            for i, p in enumerate(current_order.products, 1):
                print(f"{i}. {p.name}")
            try:
                idx = int(input("Введіть номер товару для видалення: ")) - 1
                if 0 <= idx < len(current_order.products):
                    product = current_order.products[idx]
                    current_order.remove_product(product)
                    print(f"{product.name} видалено.")
                else:
                    print("Невірний індекс.")
            except Exception as e:
                print("Помилка:", e)

        elif choice == "4":
            total = current_order.calculate_total()
            logged_user.place_order(current_order)
            print(f"Замовлення оформлено. Загальна сума: {total} грн")
            order_counter += 1
            current_order = Order(order_counter, logged_user)

        elif choice == "5":
            print("\nМої замовлення:")
            for order in logged_user.view_orders():
                print(f"\nЗамовлення №{order.order_id} — Статус: {order.status}")
                for p in order.products:
                    print(f"- {p.name} — {p.price} грн")
                print(f"Сума: {order.calculate_total()} грн")

        elif choice == "0":
            print("Вихід в головне меню.")
            break

        else:
            print("Невірна дія.")

if __name__ == "__main__":
    main()
