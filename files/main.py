from guesses import Guesses
from lotto import Lotto
from rock import Rock
from menu import Menu
from menu_game import GameMenu

while True:
    menu = GameMenu()
    if not menu.ask_to_play(): break
    
    game = menu.choose_game()
    if game == 'guesses': Guesses().play()
    elif game == 'lotto': Lotto().display()
    elif game == 'rock': Rock().play()

    good_bye = Menu()
    good_bye.add_item('\nWould you like to quit? Enter yes or no! ', 'yes', 'no')
    if good_bye.render() == 'yes': print('Thank you for your time! Good bye and have a nice day!'); break
    print("Thank you for chosing us to play again!\n"); continue