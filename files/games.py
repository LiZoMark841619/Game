from players import Player
from methods import get_valid_number
from abc import ABC, abstractmethod

class Game(ABC):

    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'

    def set_num_of_players(self, nums: int) -> None:
        self.nums = nums

    def get_num_of_players(self) -> str:
        return [Player() for _ in range(self.nums)]

    def settings(self) -> str:
        num_of_players = self.set_num_of_players((get_valid_number('How many players are going to play? ', 1, 4)))
        players = self.get_num_of_players()
        for player in players:
            player.set_name(input('Enter your name! '))
        return players

    @abstractmethod
    def some_method(self):
        pass