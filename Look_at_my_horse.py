from typing import *
def get_word_indices(strings) -> dict:
    r = dict()
    for i in range(len(strings)):
        for w in strings[i].split():
            if w.lower() not in r:
                r[w.lower()] = [i]
            else:
                r[w.lower()].append(i)


    return r

print(get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']))
