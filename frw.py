from typing import Optional

def first_repeated_word(s: Optional [str]) -> str:
    "Find first repeat"
    lst = s.split()
    res = list()
    for w in lst:
        if w in res:
            return w
        else:
            res.append(w)

    return None
