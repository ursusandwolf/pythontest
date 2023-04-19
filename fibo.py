def fibo(n):
    if n in cache:
        return cache[n]
    cache[n] = fibo(n - 1) + fibo(n - 2)
    return cache[n]


cache = {0: 0, 1: 1}
for i in range(500):
    print(i, fibo(i))
