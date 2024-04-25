from players import Player

class Game:
    
    def __str__(self) -> str:
        return f'Game: {self.__class__.__name__}'
    
    def set_num_of_players(self, numbers: int) -> None:
        self.nums = numbers
        
    def get_num_of_players(self) -> str:
        return [Player() for _ in range(self.nums)]