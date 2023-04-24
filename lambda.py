adding_10 = lambda x: x+10
print(adding_10(4))

starts_with = lambda s: True if s.startswith('W') else False
print(starts_with("winter"))

sale_lambda = lambda x: x*0.9 if x > 50 else x
print(sale_lambda(51))

sq = lambda x, y : x**2 + y**2
print(sq(4, 7))

average = lambda *x : sum(x)/len(x)
print(average(2,4,8,10))
