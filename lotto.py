import random
from games import Game
from methods import get_valid_number

class Lotto(Game):
    
    def play(self) -> list:
        guesses = set()
        while len(guesses) < 5:  
            guess = get_valid_number(prompt='Enter your number from 1 to 90! ', value_min=1, value_max=90)
            if guess in guesses:
                print('SameNumberError: Try again!!\n ')
            guesses.add(guess)
        winning_nums = set(random.sample(range(1, 91), 5))
        return guesses, winning_nums