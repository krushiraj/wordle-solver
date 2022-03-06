from random import randint, shuffle
from utils.sort import sort_words
from utils.constants import VALID, INVALID
from utils.words import words


class Node:
    def __init__(self, char):
        self.char = char
        self.validity = VALID
        self.allow_repeat = True
        self.next = [None for i in range(26)]


class TrieCollection:
    def __init__(self):
        self.tries = [None for j in range(26)]

    def build_tries(self):
        for word in words:
            self.add_word(word)

    def add_word(self, word, prev_node=None):
        if len(word) == 0:
            return

        position = ord(word[0]) - ord('a')
        current_node = None
        if prev_node is None:
            if self.tries[position] is None:
                self.tries[position] = Node(word[0])
            current_node = self.tries[position]
        else:
            current_node = prev_node.next[position] if prev_node.next[position] else Node(
                word[0])
            prev_node.next[position] = current_node

        self.add_word(word[1:], current_node)

    def do_not_repeat_char(self, char, node=None):
        if node is None:
            for i in range(len(self.tries)):
                if self.tries[i] is not None:
                    self.do_not_repeat_char(char, self.tries[i])
            return

        if node.char == char:
            node.allow_repeat = False
        for i in range(len(node.next)):
            if node.next[i] is not None:
                self.do_not_repeat_char(char, node.next[i])

    def do_not_repeat_chars(self, chars):
        for char in chars:
            self.do_not_repeat_char(char)

    def invalidate_char(self, char, node=None):
        if node is None:
            for i in range(len(self.tries)):
                if self.tries[i] is not None:
                    self.invalidate_char(char, self.tries[i])
            return

        if node.char == char:
            node.validity = INVALID
        for i in range(len(node.next)):
            if node.next[i] is not None:
                self.invalidate_char(char, node.next[i])

    def invalidate_chars(self, chars):
        for char in chars:
            self.invalidate_char(char)

    def invalidate_char_by_position(self, char, position, curr_position, node=None):
        if node is None:
            for i in range(len(self.tries)):
                if self.tries[i] is not None:
                    self.invalidate_char_by_position(
                        char, position, curr_position + 1, self.tries[i])
            return

        if node.char == char and curr_position == position:
            node.validity = INVALID
            return

        for i in range(len(node.next)):
            if node.next[i] is not None:
                self.invalidate_char_by_position(
                    char, position, curr_position+1, node.next[i])

    def invalidate_chars_by_position(self, char_position_tuples):
        for char, position in char_position_tuples:
            self.invalidate_char_by_position(char, position, -1)

    def get_word(self, word_so_far, letters_present_in_word):
        possible_words = []
        self.get_possible_words(
            word_so_far, '', 0, self.tries, letters_present_in_word, possible_words)
        return sort_words(possible_words)[0]

    def has_expected_letters(self, possibility, letters_present_in_word):
        possiblity_chars = list(possibility)
        for char in letters_present_in_word:
            if char not in possiblity_chars:
                return False
            index = possiblity_chars.index(char)
            # this helps to be sure about repeating letters in answer
            possiblity_chars = possiblity_chars[:index] + \
                possiblity_chars[index + 1:]
        return True

    def get_possible_words(self, word_to_match, possibility, idx, current_node, letters_present_in_word, word_list):
        if current_node is None:
            return

        if idx == len(word_to_match) and self.has_expected_letters(possibility, letters_present_in_word):
            word_list.append(possibility)
            return

        for i in range(26):
            if current_node[i] is not None and current_node[i].validity == VALID:
                if word_to_match[idx] == '_':
                    if not current_node[i].allow_repeat and current_node[i].char in possibility:
                        continue
                    self.get_possible_words(
                        word_to_match, possibility + current_node[i].char, idx + 1, current_node[i].next if current_node[i] is not None else None, letters_present_in_word, word_list)
                elif word_to_match[idx] == current_node[i].char:
                    self.get_possible_words(
                        word_to_match, possibility + current_node[i].char, idx + 1, current_node[i].next if current_node[i] is not None else None, letters_present_in_word, word_list)


def get_tries_root():
    root = TrieCollection()
    root.build_tries()
    return root
