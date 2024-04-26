import random
from games import Game
from players import Player
from methods import get_valid_number, get_valid_str

class Rock(Game):
    
    def settings(self) -> list:
        self.set_num_of_players(1)
        player = Player()
        player.set_name(input('Enter your name! '))
        return player

    def play(self) -> str:
        player = self.settings()
        start = 0
        num_of_games = get_valid_number('Enter the number of games you would like to play (1-5)! ', 1, 5)

        while start < num_of_games:
            options = ['rock', 'paper', 'scissors']
            comp_answ, answs = random.choice(options), []
            question = get_valid_str(f'{player.get_name()} chose from {options}! ', *options)
            answs.extend([question, comp_answ])
            start += 1
            print(f'{player.get_name()} you won, Computer chose {comp_answ}! ' if (answs[0] == 'rock' and answs[1] not in ['rock', 'paper']) or 
            (answs[0] == 'paper' and answs[1] not in ['paper', 'scissors'])or answs[0] == 'scissors' and answs[1] not in ['scissors', 'rock']
            else f'Even! Computer chose {comp_answ}. Try again! ' if answs[0] == answs[1] else f'{player.get_name()} lost, Computer chose {comp_answ}.')
    
    def some_method(self): pass