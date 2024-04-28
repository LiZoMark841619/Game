from valids import Valids
from typing import Any 
class Menu(Valids):
    
    def __init__(self) -> None:
        pass
    
    def addItem(self, question: str, value_1: Any, value_2: Any):
        if type(value_1) and type(value_2) == 'int':
            self.get_valid_number(question, value_1, value_2)
        elif type(value_1) and type(value_2) == 'str':
            self.get_valid_str(question, value_1, value_2)
        
    def set_choice(self, num: int) -> None:
        self.num = num
    
    def get_choice(self) -> int:
        return self.num