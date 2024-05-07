from valids import Valid
from typing import Any

class Menu(Valid):
    
    def add_item(self, request: str, *args: Any) -> None :
        self.request = self.get_valid_string(request, *args)
    
    def render(self) -> str:
        return self.request