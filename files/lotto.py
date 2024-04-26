import random
from games import Game
from methods import get_valid_number

class Lotto(Game):
    
    def play(self) -> tuple:
        guesses = set()
        while len(guesses) < 5:  
            guess = get_valid_number(prompt='Enter your number from 1 to 90! ', value_min=1, value_max=90)
            if guess in guesses:
                print('SameNumberError: Try again!!\n ')
            guesses.add(guess)
        winning_nums = set(random.sample(range(1, 91), 5))
        return guesses, winning_nums
    
    def display(self) -> str:
        guesses, winning_nums = self.play()
        print(f'\nWinning numbers: {winning_nums} - Your numbers: {guesses}\n')
        good_nums = len(guesses & winning_nums)
        if good_nums == len(winning_nums): print('CONGRATULATIONS! YOU WON THE LOTTERY! ')
        print(f'You have {good_nums} match(es).')
        
    def some_method(self): pass