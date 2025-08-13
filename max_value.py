# program to find the maximum value in a list - [ Assume the list is non-empty]


def max_value(nums):
    max = float("-inf")

    for num in nums:
        if num > max:
            max = num

    return max


# test
res = max_value([3, 5, 10, 2, 4])
print(res)  # 10

# time complexity: O(n)
# space complexity: O(1)
