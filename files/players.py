class Player:
    
    def set_name(self) -> None:
        while True:
            name = input('Enter your name! ')
            if len(name) >= 3: self.name = name; return
            print('Your name must be 3 character long at least! Try again! ')
        
    def get_name(self) -> str:
        return self.name