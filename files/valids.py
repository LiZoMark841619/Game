class InstanceTree:
    def __str__(self):
        return f'Object created from {self.__class__.__name__} class with attributes: {self.attrs_()}'
    
    def attrs_(self):
        for attr in self.__dict__: 
            print(attr, '->', self.__dict__[attr])
            
class Valid(InstanceTree):
    def get_valid_number(self, prompt: str, value_min: int, value_max: int) -> int:
        while True:
            try: 
                value = int(input(prompt))
                if value_min <= value <= value_max: 
                    return value
                print('The number is out of range. Try again!\n')
            except ValueError: print('Invalid value. Try again!\n')

    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args: return value
            print('Invalid value. Try again!\n')