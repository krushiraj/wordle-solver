from string import ascii_lowercase

def vowel_count(word):
    print(word, -sum([1 if char in 'aeiou' else 0 for char in word]))
    return sum([1 for char in set(word) if char in 'aeiou'])

def repitition_count(word):
    count_map = dict(zip(ascii_lowercase, [0]*len(ascii_lowercase)))
    for char in word:
        count_map[char] += 1 if count_map[char] == 0 else 2
    print(word, sum(count_map.values()))
    return sum(count_map.values())

def sort_words(words):
    return sorted(words, key=lambda x: (repitition_count(x), -vowel_count(x)))
