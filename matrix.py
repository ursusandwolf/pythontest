def create_matrix(size = 3, up_fill = 0, down_fill = 0):
    result = []
    counter = 0
    for i in range(size):
        result.append([])
        for j in range(size):
            if i == j :
                counter +=1
                result[i].append(counter)
            if i < j :
                result[i].append(up_fill)
            if i > j :
                result[i].append(down_fill)
    return result


print(create_matrix())
print(create_matrix(1))
print(create_matrix(4,9,-11))
