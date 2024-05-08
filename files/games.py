import random
from settings import Player, Game

class Guesses(Game):
    
    def game_set(self) -> tuple:
        self.set_num_of_players(); self.set_players()
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
                
class Lotto(Game):
    
    def play(self) -> tuple:
        guesses: set[int] = set()
        while len(guesses) < 5:  
            guess = self.get_valid_number('Enter your number from 1 to 90! ', 1, 90)
            if guess in guesses: print('SameNumberError: Try again!\n')
            guesses.add(guess)
        winning_nums = set(random.sample(range(1, 91), 5))
        print(f'\nWinning numbers: {winning_nums} - Your numbers: {guesses}\n')
        good_nums = len(guesses & winning_nums)
        if good_nums == len(winning_nums): print('CONGRATULATIONS! YOU WON THE LOTTERY! ')
        print(f'You have {good_nums} match(es).')
        
class Rock(Game):
    
    def game_set(self) -> tuple:
        player = Player()
        player.set_name()
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