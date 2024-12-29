from valids import Valid

class Player:
    def __init__(self) -> None:
        while True:
            name = input('Enter your name! ').title()
            if len(name) >= 3 and name.isalpha():
                self.__name = name
                return
            print('Your name must be 3 character long at least and only letters are allowed! Try again! ')
        
    def get_name(self) -> str:
        return self.__name
    
class Game(Valid):
    def set_num_of_players(self) -> None:
        self.__nums = self.get_valid_number('How many players are going to play? Set from 1 to 4! ', 1, 4)

    def get_num_of_players(self) -> int:
        return self.__nums
    
    def set_players(self) -> None:
        self.__players = [Player() for _ in range(self.get_num_of_players())]
        
    def get_players(self) -> list:
        return self.__players