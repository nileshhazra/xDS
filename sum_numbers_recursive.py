def sum_numbers_recursive(n):
    if len(n) == 0:
        return 0
    return n[0] + sum_numbers_recursive(n[1:])


res = sum_numbers_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(res)
