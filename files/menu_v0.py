from games import Game
from valids import Valids

class Menu(Valids):
    
    def __init__(self, choice: int,
    options: dict={
                     0:'Ask to play',
                     1:'Chose the game',
                     2:'Number of players',
                     3:'Names of players',
                     4: 'Good bye'}) -> None:
        
        self.options = options
        if choice in options:
            self.choice = choice
            self.menu = options[choice]
        else:
            raise ValueError('There is no such option in the Menu! ')             
            
    def __repr__(self) -> str:
        return f'Menu({self.options})'

    def ask_to_play(self) -> bool:
        question = self.get_valid_str('Would you like to play? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': return True
        else: print("Understood, good bye!"); return False
    
    def chose_game(self) -> bool:
        game = self.get_valid_str(f'Chose from {[cls.__name__ for cls in Game.__subclasses__()]}! ', 'guesses', 'lotto', 'rock')
        print(f'Welcome to my {game.title()} game! ')
        
    def set_players(self) -> int:
        self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)
    
    def want_to_quit(self) -> bool:
        question = self.get_valid_str('Would you like to quit? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': print('Understood, good bye!'); return True
        else: print("OK, let's get going!"); return False

    def display(self):
        
        if self.choice == 0:
            self.ask_to_play()
        
        elif self.choice == 1:
            self.chose_game()
            
        elif self.choice == 2:
            self.set_players()
        
        elif self.choice == 4:
            self.want_to_quit()