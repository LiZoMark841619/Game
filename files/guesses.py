from games import Game
import random
from methods import get_valid_number, get_valid_str

class Guesses(Game):
    
    def settings(self) -> str:
        num_of_players = self.set_num_of_players((get_valid_number('How many players are going to play? ', 1, 4)))
        players = self.set_game()
        
        for player in players: 
            player.set_name(input('Enter your name! '))
        
        return players
    
    def play(self):
        players = self.settings()
        count = 0
        random_number = random.randint(1, 100)
        
        while True:
            count += 1
            for player in players:
                guess = get_valid_number(f'Enter your number {count} guess {player.get_name()}! ', 1, 100)
                if guess < random_number: print('You number is less than I thought!\n ')
                elif guess > random_number: print('Your number is greater than I thought!\n')
                else: print(f'You just hit, {player.get_name()} won. '); return
                    
            quit_continue = get_valid_str('Enter q or c to quit or continue! ', 'q', 'c')
            if quit_continue == 'q': break
            if quit_continue == 'c': continue