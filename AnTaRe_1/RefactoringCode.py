def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def main():            #Можливо main почав виглядати більш не зрозуміло, але в ньому тепер менше логіки
    operations = {
        "1": ("Addition", add), #Додавши словник для вибору операцій, Я позбувся магічних чисел
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    while True:             #Виділив окрему функцію для обробки введення
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
        choice = input("Choose an operation: ")

        if choice == "5":
            break

        if choice in operations:
            num1, num2 = get_numbers()
            print("Result:", operations[choice][1](num1, num2))
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
