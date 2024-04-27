class Valids:
    
    def get_valid_number(self, prompt: str, value_min: int, value_max: int) -> int:
        while True:
            try: 
                value = int(input(prompt))
                if value_min <= value <= value_max: return value
                else: print('The number is out of range.\n')
            except ValueError: print('Enter a valid number!\n')

    def get_valid_str(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args: return value
            else: print('Invalid value. Try again! ')
            
    def ask_to_play(self) -> bool:
        question = self.get_valid_str('Would you like to play? Enter yes or no? ', 'yes', 'no')
        if question == 'yes': return True
        else: print("Understood, good bye!"); return False