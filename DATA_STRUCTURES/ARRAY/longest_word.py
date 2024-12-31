import re

def LongestWord(sen): 
    matched = re.findall(r"\w+", sen)
    longest_word = ""
    for word in matched:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = "fun&!! time"
print(LongestWord(sentence))

sentence = "I love dogs"
print(LongestWord(sentence))

sentence = "Hello world123 567"
print(LongestWord(sentence))