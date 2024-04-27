from guesses import Guesses
from lotto import Lotto
from rock import Rock
from valids import Valids
from menu import Menu

menu = Menu()
print(menu)
menu.set_choice(menu.get_valid_number('Enter a number from 0 - 4 from the menu! ', 0, 4))

menu.display()
    
game = Valids().get_valid_str('Chose from Guesses, Lotto and Rock! ', 'guesses', 'lotto', 'rock')
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