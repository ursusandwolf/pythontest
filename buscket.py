n = int(input())
d = dict()
for i in range(n):
    l = input()
    if l in d:
        d[l] += 1
    else:
        d[l] = 1

counter = 0
ld = len(d)
for item in sorted(d.items(), key=lambda pair: int(pair[1]), reverse=True):
    if counter == 0 or counter == ld-1:
        print(f"{item[0]}, {item[1]}")
    if ld == 1:
        print(f"{item[0]}, {item[1]}")
    counter +=1
