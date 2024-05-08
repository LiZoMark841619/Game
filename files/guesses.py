import random
from games import Game

class Guesses(Game):
    
    def game_set(self) -> tuple:
        self.set_num_of_players()
        self.set_players()
        players = self.get_players()
        for player in players: player.set_name()
        return players, random.randint(1, 100), 0
        
    def play(self) -> None:
        players, random_number, count = self.game_set()
        print('I thought of a number from 1 to 100! Find out what is it! ')
        while True:
            count += 1
            for player in players:
                guess = self.get_valid_number(f'{player.get_name()}, enter your No. {count} guess! ', 1, 100)
                if guess < random_number: print('You number is less than I thought!\n ')
                elif guess > random_number: print('Your number is greater than I thought!\n')
                else: print(f'You just hit, {player.get_name()} won. '); return