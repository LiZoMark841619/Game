import random
from games import Game
from players import Player

class Rock(Game):
    
    def game_set(self) -> tuple:
        player = Player()
        player.set_name(input('Enter your name! '))
        return player, self.get_valid_number('Enter the number of games you would like to play (1-5)! ', 1, 5)

    def play(self) -> None:
        player, num_of_games = self.game_set()
        for _ in range(num_of_games):
            options = ['rock', 'paper', 'scissors']
            comp_answ, answs = random.choice(options), []
            question = self.get_valid_string(f'{player.get_name()} chose from {options}! ', *options)
            answs.extend([question, comp_answ])
            
            print(f'{player.get_name()} you won, Computer chose {comp_answ}! '
            if (answs[0] == 'rock' and answs[1] not in ['rock', 'paper'])
            or (answs[0] == 'paper' and answs[1] not in ['paper', 'scissors'])
            or answs[0] == 'scissors' and answs[1] not in ['scissors', 'rock']
            else f'Even! Computer chose {comp_answ}. ' if answs[0] == answs[1]
            else f'{player.get_name()} you lost, Computer chose {comp_answ}.')