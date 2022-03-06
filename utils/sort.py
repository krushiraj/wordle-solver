def vowel_count(word):
    return sum([1 for char in set(word) if char in 'aeiou'])


def sort_words_by_vowel_count(words):
    return sorted(words, key=lambda x: (-vowel_count(set(x)), x))
