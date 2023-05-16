def gen_squares(n):
    for i in range (n):
        yield (i+1)**2

for i in gen_squares(5):
    print(i)
