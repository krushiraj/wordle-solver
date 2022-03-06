import os
from random import random
import string
from random import randint
from utils.constants import CORRECT, REPEATED, VALID, INVALID
from utils.words import total_num_words, words
from tries import get_tries_root

DEBUG = os.environ.get('DEBUG', False)

game_state = [[[None, None] for j in range(5)] for i in range(6)]
total_chances = 6
letters = zip(string.ascii_lowercase, [
              VALID for i in range(0, len(string.ascii_lowercase))])
words_root = get_tries_root()


def get_first_word():
    return words[randint(0, total_num_words - 1)]


def get_word(current_state, is_first_word):
    if is_first_word:
        return get_first_word()

    word_so_far, valid_chars = update_state_and_graph(current_state)
    print('Correct Letters in word so far: {}'.format(' '.join(word_so_far)))
    return words_root.get_word(word_so_far, valid_chars)


def update_state_and_graph(current_state):
    word_so_far = []
    invalid_chars = []
    invalid_by_position = []
    valid_chars = []
    idx = 0
    for letter, validity in current_state:
        if validity == CORRECT:
            word_so_far.append(letter)
        else:
            word_so_far.append('_')

        if validity == INVALID:
            invalid_chars.append(letter)
        elif validity == VALID:
            valid_chars.append(letter)
            invalid_by_position.append((letter, idx))
        idx += 1

    words_root.invalidate_chars(invalid_chars)
    words_root.invalidate_chars_by_position(invalid_by_position)
    return word_so_far, valid_chars


def guess_word(current_state, guess_random_word=False):
    if guess_random_word:
        return 'audio'
    print('Guessing the words')
    is_first_word = current_state is None
    word = get_word(current_state, is_first_word)
    print('Word: {}'.format(word.upper()))
    print('\n')
    return word


def check_end_game(idx):
    for char, validity in game_state[idx]:
        if validity != CORRECT:
            return False
    return True


def clean_result(result, word):
    final_result = [None for i in range(len(word))]
    repeated_chars = []
    for i in range(len(word)):
        if result[i] == INVALID and word[i] in word[:i]:
            final_result[i] = REPEATED
            repeated_chars.append(word[i])
        else:
            final_result[i] = result[i]
    words_root.do_not_repeat_chars(repeated_chars)
    return final_result


def handle_first_chance_input():
    print('We can always start the first guess with "AUDIO" word, else you can choose to go with a random word')
    char = input('Do you want to start with a random word? (y/n): ')
    if char[0].lower() == 'y':
        return True
    return False


def run_game_loop(chances=total_chances):
    print('Game loop started')
    for chance_num in range(total_chances-chances, total_chances):
        print('Chance number: {}'.format(chance_num+1))
        if DEBUG:
            print('Game state: {}'.format(game_state))
            print('\n')

        # AUDIO words is the only word in answer list that has highest vowel count
        # so we can use it to check what vowel does the answer have
        guess_random_word = handle_first_chance_input() if chance_num == 0 else False
        word = guess_word(None if chance_num ==
                          0 else game_state[chance_num-1], guess_random_word)

        result = clean_result(list(map(int, input(
            'Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): ')[:5])), word)

        game_state[chance_num] = [[word[i], result[i]]
                                  for i in range(len(word))]
        print('\n')
        if check_end_game(chance_num):
            print('Game over')
            break
    return


def load_game_state():
    print('Loading game state')
    chances = int(
        input('Enter the number of chances you have already played: '))
    chances_left = total_chances - chances

    for i in range(chances):
        print('Chance number: {}'.format(i+1))
        word = input('Enter the word: ')
        result = clean_result(list(map(int, input(
            'Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): ')[:5])), word)
        game_state[i] = [[word[i], result[i]] for i in range(len(word))]
        update_state_and_graph(game_state[i])
        print('\n')
    return chances_left
