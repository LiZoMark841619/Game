import random
from games import Game
from methods import get_valid_number, get_valid_str

class Rock(Game):
    
    def settings(self):
        self.set_num_of_players(1)
        players = self.get_num_of_players()
        for player in players: player.set_name(input('Enter your name! '))
        return players

    def play(self):
        players = self.settings()
        start = 0
        num_of_games = get_valid_number('Enter the number of games you would like to play (1-5)! ', 1, 5)

        while start < num_of_games:
            options = ['rock', 'paper', 'scissors']
            computer = random.choice(options)
            answers = []
            for player in players:
                question = get_valid_str(f'{player.get_name()} chose from {options}! ', *options)
                answers.append(question)
                answers.append(computer)
            start += 1
            print(f'{players[0].get_name()} you won! ' if (answers[0] == 'rock' and answers[1] not in ['rock', 'paper']) or 
            (answers[0] == 'paper' and answers[1] not in ['paper', 'scissors'])or answers[0] == 'scissors' and answers[1] not in ['scissors', 'rock']
            else 'Even! Try again! ' if answers[0] == answers[1] else 'Computer won! ')
    
    def some_method(self):
        pass