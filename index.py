from game import load_game_state, run_game_loop


def start():
    rand_char = (
        input("Choose an options:\n1. New Game\n2. Continue Game\n") or 'n')[0]
    if rand_char == '1':
        run_game_loop()
        return
    elif rand_char == '2':
        chances_left = load_game_state()
        run_game_loop(chances_left)
    else:
        print('Game was not started. Exiting...')
    return


start()
