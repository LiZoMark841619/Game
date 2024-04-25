from players import Player
from abc import ABC, abstractmethod

class Game(ABC):
    
    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'
    
    def set_num_of_players(self, nums: int) -> None:
        self.nums = nums
        
    def get_num_of_players(self) -> str:
        return [Player() for _ in range(self.nums)]
    
    # @abstractmethod
    # def some_method(self):
    #     pass