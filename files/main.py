import random
from player import Player
from guesses import Guesses
from lotto import Lotto
from methods import ask_to_play, get_valid_number, get_valid_str

def set_guesses() -> list:
    game_one = Guesses()
    game_one.set_num_of_players(get_valid_number('How many players are going to play? ', 1, 4))
    players = [Player() for _ in range(game_one.get_num_of_players())]
    for player in players:
        player.set_name(input('Enter your name: '))
    return players

def guesses(func: object):
    players = func()
    count = 0
    random_number = random.randint(1, 100)
    while True:
        count += 1
        for player in players:
            guess = get_valid_number(f'Enter your number {count} guess {player.get_name()}! ', 1, 100)
            if guess < random_number: print('You number is less than I thought!\n '); continue
            elif guess > random_number: print('Your number is greater than I thought!\n'); continue
            else: print(f'You just hit, {player.get_name()} won. '); break
                
        quit_continue = get_valid_str('Enter q or c to quit or continue! ', 'q', 'c')
        if quit_continue == 'q': break
        if quit_continue == 'c': continue

def lotto() -> tuple:
    game = Lotto()
    guesses = set()
    while len(guesses) < 5:  
        guess = get_valid_number(prompt='Enter your number from 1 to 90! ', value_min=1, value_max=90)
        if guess in guesses:
            print('SameNumberError: Try again!!\n ')
        guesses.add(guess)
    winning_nums = set(random.sample(range(1, 91), 5))
    return guesses, winning_nums

if ask_to_play():
    game = get_valid_str('Chose from Guesses and Lotto! ', 'guesses', 'lotto')
    print(f'Welcome to my {game} game! ')
    if game == 'guesses':
        print('I thought of a number from 1 to 100! Find out what is it! ')
        guesses(set_guesses)
    elif game == 'lotto':
        game = lotto()
        print(f'\nWinning numbers: {game[1]} - Your numbers: {game[0]}\n')
        good_nums = len(game[0] & game[1])
        if good_nums == len(game): print('CONGRATULATIONS! YOU WON THE LOTTERY! ')
        print(f'You have {good_nums} match(es).')