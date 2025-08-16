def pair_sum(numbers, target_sum):
    previous = {}
    for i in range(len(numbers)):
        compliment = target_sum - numbers[i]
        if compliment in previous:
            return (previous[compliment], i)
        previous[numbers[i]] = i
