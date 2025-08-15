from collections import Counter


def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
    # return char_count(s1) == char_count(s2)


# def char_count(s):
#     count = {}
#     for ch in s:
#         if ch not in count:
#             count[ch] = 0
#         count[ch] += 1
#     return count


print(anagrams("flat", "latf"))
print(anagrams("jsk", "latf"))
