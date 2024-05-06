from players import Player
from valids import Valid

class Game(Valid):

    def __repr__(self) -> str:
        return f'Game: {self.__class__.__name__}'

    def set_num_of_players(self) -> None:
        self.nums = self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)

    def get_num_of_players(self) -> int:
        return self.nums
    
    def make_players(self) -> list:
        return [Player() for _ in range(self.get_num_of_players())]
        
    def set_players_names(self) -> list:
        players = self.make_players()
        for player in players: player.set_name()
        return players