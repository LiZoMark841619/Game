from games import Game

class Guesses(Game):
    
    def set_num_of_players(self, numbers: int) -> None:
        self.nums = numbers
        
    def get_num_of_players(self) -> str:
        return self.nums