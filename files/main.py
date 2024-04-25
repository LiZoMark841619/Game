from guesses import Guesses
from lotto import Lotto
from rock import Rock
from methods import ask_to_play, get_valid_str

if ask_to_play():
    
    game = get_valid_str('Chose from Guesses, Lotto and Rock! ', 'guesses', 'lotto', 'rock')
    print(f'Welcome to my {game.title()} game! ')
    
    if game == 'guesses':
        test = Guesses()
        game = test.play()
        
    elif game == 'lotto':
        test = Lotto()
        game = test.display()
    
    elif game == 'rock':
        test = Rock()
        game = test.play()