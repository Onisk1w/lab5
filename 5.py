def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
print(fibonacci(10))  #55, так как 55 - это 10-ое число Фибоначчи
