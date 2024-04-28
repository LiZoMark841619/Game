from valids import Valids
from typing import Any

class Menu(Valids):
    
    def __init__(self) -> None: pass
    
    def addItem(self, request: str, opt_1: Any, opt_2: Any):
        if (type(opt_1) and type(opt_2))!= int:
            self.request = self.get_valid_str(request, opt_1, opt_2)
        elif (type(opt_1) and type(opt_2))!= str: 
            self.request = self.get_valid_number(request, opt_1, opt_2)
    
    def render(self):
        return self.request