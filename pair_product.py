def pair_product(numbers, target_product):
    previous = {}

    for index, num in enumerate(numbers):
        compliment = target_product // num
        if compliment in previous:
            return (previous[num], index)
        previous[num] = index
