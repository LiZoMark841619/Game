from valids import Valid
from typing import Any

class Menu(Valid):
            
    def __repr__(self) -> str:
        return f'Menu({self.__class__.__name__})'
    
    def addItem(self, request: str, opt_1: Any, opt_2: Any)-> None :
        self.request = self.get_valid_str(request, opt_1, opt_2)
    
    def render(self) -> str:
        return self.request