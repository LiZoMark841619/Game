from games import Game

class Guesses(Game):
    
    def set_num_of_players(self, numbers: int):
        self.nums = numbers
    def get_num_of_players(self):
        return self.nums
