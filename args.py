def count_args(*args):
    return len(args)

a,b,*c = "lsdkjfh"
print(a,b,c)
print(count_args(c))
print(count_args(a,b,c))
