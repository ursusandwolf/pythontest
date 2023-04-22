def quick_sort(lst):
    ln = len(lst)
    if ln < 2: return lst

    middle = [lst[ln//2]]
    left, right = [], []
    for i in range (ln):
        if i == ln//2:
            continue
        if lst[i] == middle[0]:
            middle.append(lst[i])
        if lst[i] < middle[0]:
            left.append(lst[i])
        if lst[i] > middle[0]:
            right.append(lst[i])

    return quick_sort(left) +middle+ quick_sort(right)

print(quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))
