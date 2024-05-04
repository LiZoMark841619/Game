from valids import Valid
from typing import Any

class Menu(Valid):
            
    def __repr__(self) -> str:
        return f'Menu({self.__class__.__name__})'
    
    def add_item(self, request: str, *args: Any) -> None :
        self.request = self.get_valid_string(request, *args)
    
    def render(self) -> str:
        return self.request