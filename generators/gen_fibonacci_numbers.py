def fibo(n):
    f = [1,1,2,3,5,8]
    if n < 1:
        return 0
    if n < 7:
        return f[n-1]
    return fibo(n-1) + fibo(n-2)

def gen_fibonacci_numbers(n):
    for i in range (n):
        yield fibo(i+1)

for i in gen_fibonacci_numbers(10):
    print(i)
