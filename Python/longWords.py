def long_word(words):
    return max(words, key=len) if words else None

print(long_word(["starberry", "blueberry", "secondberrry"]))

def longest_words(words):
    max_len = max(map(len, words)) if words else 0
    return [word for word in words if len(word) == max_len]

print(longest_words(["fives","lolsi","hi","bye"]))