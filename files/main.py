from primes import Primes
from guesses import Guesses
from lotto import Lotto
from rock import Rock
from menu import Menu
from menu_game import GameMenu

def main():
    while True:
        menu = GameMenu()
        if not menu.ask_to_play(): break
        
        game = menu.choose_game()
        for klass in [Guesses, Rock, Primes]:
            if klass.__name__ == game:
                klass().play()
        if game == 'Lotto':
            Lotto().display()

        good_bye = Menu()
        good_bye.add_item('\nWould you like to quit? Enter yes or no! ', 'yes', 'no')
        if good_bye.render() == 'yes': print('Thank you for your time! Good bye and have a nice day!'); return
        else: print("Thank you for chosing us to play again!\n")

if __name__ == '__main__':
    main()
