from string import ascii_lowercase
from random import shuffle


def vowel_count(word):
    return sum([1 for char in set(word) if char in 'aeiou'])


def repitition_count(word):
    count_map = dict(zip(ascii_lowercase, [0]*len(ascii_lowercase)))
    for char in word:
        count_map[char] += 1 if count_map[char] == 0 else 2
    return sum(count_map.values())


def sort_words(words):
    shuffle(words)
    return sorted(words, key=lambda x: (repitition_count(x), -vowel_count(x)))
