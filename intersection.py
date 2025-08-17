def intersection(a, b):
    res = []
    for i in a:
        if i in b:
            res.append(i)
    return res


# Efficient approach


def intersection_e(a, b):
    res = []
    items_set = set(a)
    for item in b:
        if item in items_set:
            res.append(item)
    return res


print(intersection_e([1, 2, 3, 4], [3, 4, 5, 6]))
