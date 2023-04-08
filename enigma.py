def shift_letter(letter, shift):
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

def enigma(s):
    res = ""
    i = 1
    for c in s:
        res += shift_letter(c, i)
        i +=1

    return res


print(shift_letter('b', 2))
print(enigma("Hello world, Hello world Hello world Hello world Hello world Hello world Hello world Hello world"))
