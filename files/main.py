from guesses import Guesses
from lotto import Lotto
from rock import Rock
from valids import Valids

if Valids.ask_to_play():
    
    game = Valids.get_valid_str('Chose from Guesses, Lotto and Rock! ', 'guesses', 'lotto', 'rock')
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