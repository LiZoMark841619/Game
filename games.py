from methods import get_valid_number
from player import Player
class Game:
    
    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'
    
    def set_num_of_players(self, numbers: int) -> None:
        self.nums = numbers
        
    def get_num_of_players(self) -> str:
        return self.nums
    
    def set_game(self) -> list:
        self.set_num_of_players((get_valid_number('How many players are going to play? ', 1, 4)))
        players = [Player() for _ in range(self.get_num_of_players())]
        for player in players: player.set_name(input('Enter your name! '))
        return players