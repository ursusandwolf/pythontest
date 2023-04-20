def flatten(l):
    """The function converts a nested list into a flat list"""
    if not l:
        return []
    if isinstance(l[0], list):
        return flatten(l[0]) + flatten(l[1:])
    return l[:1] + flatten(l[1:])


print(flatten([1,2,3,[4,5,[6]]]))
