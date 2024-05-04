from games import Game
from menu import Menu
import array
from typing import Generator

class Primes(Game):
    
    def collect_primes(self, n: int) -> Generator:
        yield from (i for i in range(2, n+1) if sum(i % k == 0 for k in range(1, int(i**0.5) + 1)) == 1)
    
    def store_primes(self, n: int) -> array.array:
        primes, container = self.collect_primes(n), array.array('Q')
        while True:
            try: container.append(next(primes))
            except StopIteration: break
        return container
    
    def store_not_primes(self, n: int) -> array.array:
        return array.array('Q', [num for num in range(n+1) if num not in self.store_primes(n)])
    
    def store_prime_factors(self, n: int) -> array.array:
        return array.array('Q', [num for num in self.store_primes(n) if n % num == 0])
    
    def collect_semi_primes(self, n: int) -> Generator:
        primes, not_primes = self.store_primes(n), self.store_not_primes(n)
        yield from (num for num in not_primes for i in range(len(primes)) for k in range(i+1) if num == primes[i] * primes[k])

    def play(self):
        self.set_num_of_players(1)
        self.set_players_names()
        num = self.get_valid_number('Enter a number from 2 to 500000! ', 2, 500000)
        menu = Menu()
        menu.add_item('Chose from [primes, factors, semi-primes] options to list the numbers! ', 'primes', 'factors', 'semi-primes')
        if menu.render() == 'primes': print(*self.store_primes(num))
        elif menu.render() == 'factors': print(*self.store_prime_factors(num))
        else: print(list(self.collect_semi_primes(num)))