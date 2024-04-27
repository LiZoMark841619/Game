from guesses import Guesses
from lotto import Lotto
from rock import Rock
from menu import Menu

menu = Menu()

if menu.ask_to_play():
    game = menu.chose_game()

    if game == 'guesses':
        Guesses().play()
        
    elif game == 'lotto':
        Lotto().play()

    elif game == 'rock':
        Rock().play()