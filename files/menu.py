from valids import Valids

class Menu(Valids):
    
    def __init__(self) -> None:
        pass
        
    def set_choice(self, num: int) -> None:
        self.num = num
    
    def get_choice(self) -> int:
        return self.num