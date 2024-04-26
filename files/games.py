from players import Player
from methods import get_valid_number
from abc import ABC, abstractmethod

class Game(ABC):

    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'

    def set_num_of_players(self, nums: int) -> None:
        self.nums = nums

    def get_num_of_players(self) -> int:
        return self.nums
    
    def make_players(self) -> list:
        return [Player() for _ in range(self.get_num_of_players())]
        
    def settings(self) -> list:
        self.set_num_of_players((get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)))
        players = self.make_players()
        for player in players:
            player.set_name(input('Enter your name! '))
        return players

    @abstractmethod
    def some_method(self): pass