from player import Player

class Game:
    
    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'
    
    def set_num_of_players(self, numbers: int) -> None:
        self.nums = numbers
        
    def get_num_of_players(self) -> str:
        return self.nums
    
    def set_game(self) -> list:
        if not self.nums:
            self.set_num_of_players(2)
        players = [Player() for _ in range(self.get_num_of_players())]
        return players