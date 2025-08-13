# longest word in a string, in case of ties, take the later word


def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""

    for word in words:
        if len(word) >= len(longest):
            longest = word

    return longest


# test
res = longest_word("life is beautiful")
print(res)

# time complexity - O(n + n ) ~ O(n)
# space complexity - O(n)
