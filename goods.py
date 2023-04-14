def print_goods(*args):
    goods = []
    for a in args:
        if type(a) == str and len(a)>0 and a != ' ':
            goods.append(a)

    if len(goods) == 0:
        print("No items")
        return
    i = 1
    for g in goods:
        print(f"{i}. {g}")
        i +=1

print_goods([], {}, 1, 2)
print_goods(1, True, ' ', '', 'Pineapple')
