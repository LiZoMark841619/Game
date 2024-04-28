from players import Player
from valids import Valids
from abc import ABC, abstractmethod

class Game(ABC, Valids):

    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'

    def set_num_of_players(self, nums: int) -> None:
        self.nums = nums

    def get_num_of_players(self) -> int:
        return self.nums
    
    def make_players(self) -> list:
        return [Player() for _ in range(self.get_num_of_players())]
        
    def set_players(self) -> list:
        players = self.make_players()
        for player in players: player.set_name(input('Enter your name! '))
        return players
    
    @abstractmethod
    def some_method(self): pass