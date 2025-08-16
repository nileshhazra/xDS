def pair_sum(numbers, target_sum):
    previous = {}
    for i in range(len(numbers)):
        compliment = target_sum - numbers[i]
        if compliment in previous:
            return (previous[compliment], i)
        previous[numbers[i]] = i


# another approach with different syntax
def pair_sum(numbers, target_sum):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_numbers:
            return (index, previous_numbers[complement])

        previous_numbers[num] = index


# time complexity - O[n]
# space complexity - O(na)
