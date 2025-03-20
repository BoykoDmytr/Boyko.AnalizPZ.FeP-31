def fact(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("Factorial:", fact(num))
if check_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
