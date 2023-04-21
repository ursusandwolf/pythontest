def flatten_dict(d:dict, prefix='') -> dict:
    """The function converts a nested dictionary into a flat one"""
    res = {}
    for k,v in d.items():
        if isinstance(v, int):
            res[prefix+k] = v
        else:
            res = {**res,  **flatten_dict(v, prefix+k+'_')}

    return res

nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}

print(flatten_dict(nested))
