from valids import Valid
from typing import Any
from settings import Game

class Menu(Valid):
    
    def add_item(self, request: str, *args: Any) -> None :
        self.request = self.get_valid_string(request, *args)
    
    def render(self) -> str:
        return self.request
    
class GameMenu(Menu):
    
    def ask_to_play(self) -> bool:
        if self.get_valid_string('Would you like to play? Enter yes/no? ', 'yes', 'no') == 'yes': return True
        print("Good bye!"); return False
    
    def choose_game(self) -> str:
        game = self.get_valid_string(f'Choose from {[cls.__name__ for cls in Game.__subclasses__()]} games! ', 'guesses', 'lotto', 'rock', 'primes')
        print(f'Welcome to my {game.title()} game! ')
        return game.title()
    
    def want_to_quit(self) -> bool:
        if self.get_valid_string('Would you like to quit? Enter yes/no? ', 'yes', 'no') == 'yes': print('Good bye!'); return True
        print("Let's get going!"); return False