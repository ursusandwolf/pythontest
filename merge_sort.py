def merge_sort(lst):
    middle = len(lst)//2
    if middle == 0:
        return lst
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return  merge_two_list(left, right)

def merge_two_list(l,r):
    res = []
    i = j = 0
    while i < (len(l)) and j < (len(r)):
        if l[i] > r[j]:
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1
    if i < len(l):
        res +=l[i:]
    if j < len(r):
        res +=r[j:]

    return res

print(merge_sort([75, 3, 4, 55, 45, 60]))
