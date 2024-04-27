from games import Game
from valids import Valids

class Menu(Valids):
    
    def __init__(self, options: dict={0:'Ask to play', 1:'Chose the game', 2:'Number of players', 3:'Names of players', 4: 'Want to quit'}) -> None:               
        self.options = options

    def __repr__(self) -> str:
        return f'Menu({self.options})'
    
    def set_choice(self, num: int) -> None:
        self.num = num
    
    def get_choice(self) -> str:
        return self.num
    
    def ask_to_play(self) -> bool:
        question = self.get_valid_str('Would you like to play? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': return True
        else: print("Understood, good bye!"); return False
    
    def chose_game(self) -> bool:
        game = self.get_valid_str(f'Chose from {[cls.__name__ for cls in Game.__subclasses__()]}! ', 'guesses', 'lotto', 'rock')
        print(f'Welcome to my {game.title()} game! ')
        return game
        
    def set_players(self) -> int:
        self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)
    
    def want_to_quit(self) -> bool:
        question = self.get_valid_str('Would you like to quit? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': print('Understood, good bye!'); return True
        else: print("OK, let's get going!"); return False

    def display(self):
        request = self.get_choice()
        
        if request == 0: self.ask_to_play()
        elif request == 1: self.chose_game()
        elif request == 2: self.set_players()
        elif request == 4: self.want_to_quit()