from menu import GameMenu
from games import Guesses, Lotto, Rock
from primes import Primes

def main():
    while True:
        menu = GameMenu()
        if not menu.ask_to_play(): break
        game = menu.choose_game()
        for klass in [Primes, Guesses, Lotto, Rock]:
            if klass.__name__ == game.title():
                klass().play()
        menu.add_item('\nWould you like to quit? Enter yes or no! ', 'yes', 'no')
        if menu.render() == 'yes': print('Thank you for your time! Good bye and have a nice day!'); return
        else: print("Thank you for chosing us to play again!\n")

if __name__ == '__main__': main()