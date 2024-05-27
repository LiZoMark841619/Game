from valids import Valid

class Player(Valid):
    def set_name(self) -> None:
        while True:
            name = input('Enter your name! ').title()
            if len(name) >= 3 and name.isalpha():
                self.name = name
                return
            print('Your name must be 3 character long at least and only letters are allowed! Try again! ')
        
    def get_name(self) -> str:
        return self.name
    
class Game(Valid):
    def set_num_of_players(self) -> None:
        self.nums = self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)

    def get_num_of_players(self) -> int:
        return self.nums
    
    def set_players(self) -> list:
        self.players = [Player() for _ in range(self.get_num_of_players())]
        
    def get_players(self) -> list:
        return self.players