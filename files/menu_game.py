from menu import Menu
from games import Game

class GameMenu(Menu):
    
    def ask_to_play(self) -> bool:
        question = self.get_valid_str('Would you like to play? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': return True
        else: print("Understood, good bye!"); return False
    
    def chose_game(self) -> str:
        game = self.get_valid_str(f'Chose from {[cls.__name__ for cls in Game.__subclasses__()]}! ', 'guesses', 'lotto', 'rock')
        print(f'Welcome to my {game.title()} game! '); return game
    
    def want_to_quit(self) -> bool:
        question = self.get_valid_str('Would you like to quit? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': print('Understood, good bye!'); return True
        else: print("OK, let's get going!"); return False