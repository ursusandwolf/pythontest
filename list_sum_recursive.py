def list_sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum_recursive(lst[1:])

print(list_sum_recursive([1,2,3]))
