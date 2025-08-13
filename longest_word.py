# longest word in a string


def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""
    for word in words:
        if len(word) >= len(longest):
            longest = word
            word_length = len(word)

    return longest


# test
res = longest_word("life is beautiful")
print(res)

# time complexity - O(n + n ) ~ O(n)
# space complexity - O(n)
