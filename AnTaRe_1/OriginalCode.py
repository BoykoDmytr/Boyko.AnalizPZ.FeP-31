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


def main():      #Велика складність у main() – забагато логіки в одному місці.
    while True:                      #Магічні числа – вибір операцій здійснюється за числовими значеннями ("1", "2", ...).
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Choose an operation: ")

        if choice == "5":
            break

        num1 = float(input("Enter first number: ")) #Дублювання коду – аналогічна структура для кожної операції.
        num2 = float(input("Enter second number: ")) #Дублювання коду – аналогічна структура для кожної операції.

        if choice == "1":                            #Дублювання коду – аналогічна структура для кожної операції.
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()