def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def trailing_zeros(n):
    f = factorial(n)
    n = 0
    while f % 10 == 0:
        n += 1
        f //= 10
    return n


print(trailing_zeros(30))
