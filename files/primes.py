from players import Player
from games import Game
from menu import Menu
from typing import Generator
from array import array

class Primes(Game):
    
    def collect_primes(self, n: int) -> Generator:
        yield from (i for i in range(2, n+1) if sum(i % k == 0 for k in range(1, int(i**0.5) + 1)) == 1)
    
    def store_primes(self, n: int) -> array:
        primes, container = self.collect_primes(n), array('Q')
        while True:
            try: container.append(next(primes))
            except StopIteration: break
        return container
    
    def store_not_primes(self, n: int) -> array:
        return array('Q', [num for num in range(n+1) if num not in self.store_primes(n)])
    
    def store_prime_factors(self, n: int) -> array:
        return array('Q', [num for num in self.store_primes(n) if n % num == 0])
    
    #It is an advanced problem to be solved in CodeCademy.
    def collect_semi_primes(self, n: int) -> Generator:
        primes, not_primes = self.store_primes(n), self.store_not_primes(n)
        yield from (num for num in not_primes for i in range(len(primes)) for k in range(i+1) if num == primes[i] * primes[k])

    def game_set(self):
        player = Player()
        player.set_name()
        return player
    
    def play(self):
        player = self.game_set()
        num = self.get_valid_number('Enter a number from 2 to 500000! ', 2, 500000)
        menu = Menu()
        menu.add_item(f'{player.get_name()}, chose from [primes, factors, semi-primes] to list numbers! ', 'primes', 'factors', 'semi-primes')
        if menu.render() == 'primes': print(*self.store_primes(num))
        elif menu.render() == 'factors': print(*self.store_prime_factors(num))
        else: print(list(self.collect_semi_primes(num)))