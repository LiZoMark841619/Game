from guesses import Guesses
from lotto import Lotto
from methods import ask_to_play, get_valid_str

if ask_to_play():
    
    game = get_valid_str('Chose from Guesses and Lotto! ', 'guesses', 'lotto')
    print(f'Welcome to my {game} game! ')
    
    if game == 'guesses':
        print('I thought of a number from 1 to 100! Find out what is it! ')
        test = Guesses()
        game = test.play()
        
    elif game == 'lotto':
        test = Lotto()
        game = test.play()
        print(f'\nWinning numbers: {game[1]} - Your numbers: {game[0]}\n')
        good_nums = len(game[0] & game[1])
        if good_nums == len(game): print('CONGRATULATIONS! YOU WON THE LOTTERY! ')
        print(f'You have {good_nums} match(es).')