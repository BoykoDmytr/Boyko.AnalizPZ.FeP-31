import math

def factorial(n: int) -> int:
    """Обчислює факторіал числа."""
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел.")
    return math.prod(range(1, n + 1))

def is_prime(n: int) -> bool:
    """Перевіряє, чи є число простим."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """Головна функція програми."""
    try:
        num = int(input("Enter a number: "))
        print("Factorial:", factorial(num))
        print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
