def most_frequent_char(s):
    count = {}
    for ch in s:
        if ch not in count:
            count[ch] = 0
        count[ch] += 1

    most_frequent = None
    max_count = 0
    for ch in s:
        if count[ch] > max_count:
            max_count = count[ch]
            most_frequent = ch

    return most_frequent


print(most_frequent_char("hgvbgffff"))


# from collections import Counter

# def most_frequent_char(s):
#   count = Counter(s)
#   best = None
#   for char in s:
#     if best is None or count[char] > count[best]:
#       best = char
#   return best
