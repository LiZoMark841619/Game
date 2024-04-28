from guesses import Guesses
from lotto import Lotto
from rock import Rock
from menu import Menu
from menu_game import GameMenu

while True:
    
    menu = GameMenu()
    if not menu.ask_to_play(): break
    else:
        game = menu.chose_game()

        if game == 'guesses':
            Guesses().play()
            
        elif game == 'lotto':
            Lotto().play()

        elif game == 'rock':
            Rock().play()

    good_bye = Menu()
    good_bye.addItem('Would you like to quit? Enter yes or no! ', 'yes', 'no')
    if good_bye.render() == 'yes':
        print('Thank you for your time and being with! Good bye! Have a nice day!'); break
    else:
        print('Ok, let us restart the game from the begining! '); continue