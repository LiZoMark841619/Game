from menu import Menu
from games import Game

class GameMenu(Menu):
    
    def ask_to_play(self) -> bool:
        if self.get_valid_string('Would you like to play? Enter yes or no? ', 'yes', 'no') == 'yes': return True
        print("Understood. Good bye!")
    
    def choose_game(self) -> str:
        game = self.get_valid_string(f'Choose from {[cls.__name__ for cls in Game.__subclasses__()]}! ', 'guesses', 'lotto', 'rock')
        print(f'Welcome to my {game.title()} game! '); return game
    
    def want_to_quit(self) -> bool:
        if self.get_valid_string('Would you like to quit? Enter yes or no? ', 'yes', 'no') == 'yes': print('Understood, good bye!'); return True
        print("OK, let's get going!")