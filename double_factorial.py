def double_factorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * double_factorial(n - 2)

print(double_factorial(int(input())))
