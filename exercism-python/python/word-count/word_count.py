import re
from collections import Counter

def count_words(sentence):
    words = []
    counter = {}

    for letter in sentence.lower():
        if letter.isalnum() or letter == "'":
            words.append(letter)
        else:
            words.append(' ')

    for word in ''.join(words).split():
        word = word.strip("'")
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter
