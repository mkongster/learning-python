'''Counts the occurences of words in a file and returns the most and least occuring words
'''

from quick_python.ch6.lab6 import clean_text
from operator import itemgetter

import sys

def count_words(list_of_words: list) -> dict:
    occurences = {}
    for word in list_of_words:
        occurences[word] = occurences.get(word, 0) + 1
    return occurences
    
def get_max_value(dict_of_values: dict) -> (str, int):
    values = dict_of_values.items()
    return sorted(values, key=itemgetter(1))[-1]

def get_min_value(dict_of_values: dict) -> (str, int):
    values = dict_of_values.items()
    return sorted(values, key=itemgetter(1))[0]

def main():
    clean_words = clean_text(False)
    count_of_words = count_words(clean_words)
    most, most_count = get_max_value(count_of_words)
    least, least_count = get_min_value(count_of_words)
    print('The most common word is: {most} with {most_count} occurences.' \
        .format(most=most, most_count=most_count))
    print('The least common word is: {least} with {least_count} occurences.' \
        .format(least=least, least_count=least_count))

