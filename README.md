# wordle-solver
 A script to solve wordle without statistics and ML. Just by word memory and heuristics.


# How to use this

- Just clone the repo [krushiraj/wordle-solver](https://github.com/krushiraj/wordle-solver)
- Make sure your current working directory is in the root directory of this repo

```bash
python3 index.py
```
That is all required to run this. No other dependencies required. I have run this using python3 but I believe this should also work with python2.

## Example output
> The word this script is going to guess is 'SOLVE'
```bash
~/PWD/wordle-solver git:(main)
python3 index.py
Choose an options:
1. New Game
2. Continue Game
1
Game loop started
Chance number: 0
Guessing the words
Word: INANE


Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): 00002


Chance number: 1
Guessing the words
Correct Letters in word so far: _ _ _ _ e
Word: BOULE


Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): 02012


Chance number: 2
Guessing the words
Correct Letters in word so far: _ o _ _ e
Word: LODGE


Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): 12002


Chance number: 3
Guessing the words
Correct Letters in word so far: _ o _ _ e
Word: SOLVE


Enter the result of the word: (GREY = 0, YELLOW = 1, GREEN = 2): 22222


Game over
```

The code and approach is very heuristic and naive.

> PS: If you think you can improve performance or algo, please feel free to raise a PR.