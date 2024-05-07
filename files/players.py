from instancetree import InstanceTree

class Player(InstanceTree):
    
    def set_name(self) -> None:
        while True:
            name = input('Enter your name! ').title()
            if len(name) >= 3 and name.isalpha(): self.name = name; return
            print('Your name must be 3 character long at least and only letters are allowed! Try again! ')
        
    def get_name(self) -> str:
        return self.name