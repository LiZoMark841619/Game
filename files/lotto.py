import random
from games import Game

class Lotto(Game):
    
    def play(self) -> tuple:
        guesses = set()
        while len(guesses) < 5:  
            guess = self.get_valid_number('Enter your number from 1 to 90! ', 1, 90)
            if guess in guesses:
                print('SameNumberError: Try again!!\n ')
            guesses.add(guess)
        winning_nums = set(random.sample(range(1, 91), 5))
        print(f'\nWinning numbers: {winning_nums} - Your numbers: {guesses}\n')
        good_nums = len(guesses & winning_nums)
        if good_nums == len(winning_nums): print('CONGRATULATIONS! YOU WON THE LOTTERY! ')
        print(f'You have {good_nums} match(es).')