import random
from games import Game

class Guesses(Game):
    
    def play(self) -> str:
        self.set_num_of_players(self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4))
        players = self.settings()
        count = 0
        random_number = random.randint(1, 100)
        
        print('I thought of a number from 1 to 100! Find out what is it! ')

        while True:
            count += 1
            for player in players:
                guess = self.get_valid_number(f'{player.get_name()}, enter your guess No. {count}! ', 1, 100)
                if guess < random_number: print('You number is less than I thought!\n ')
                elif guess > random_number: print('Your number is greater than I thought!\n')
                else: print(f'You just hit, {player.get_name()} won. '); return
                    
            quit_continue = self.get_valid_str('Enter q or c to quit or continue! ', 'q', 'c')
            if quit_continue == 'q': break
            if quit_continue == 'c': continue
    
    def some_method(self): pass