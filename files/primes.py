from games import Game
import array
from typing import Generator

class Primes(Game):
    
    def collect_primes(self, n: int) -> Generator:
        yield from (i for i in range(2, n+1) if sum(i % k == 0 for k in range(1, int(i**0.5) + 1)) == 1)
    
    def contain_primes(self, n: int) -> array.array:
        primes, container = self.collect_primes(n), array.array('Q')
        while True:
            try: container.append(next(primes))
            except StopIteration: break
        return container
    
    def contain_not_primes(self, n: int) -> array.array:
        return array.array('Q', [num for num in range(n+1) if num not in self.contain_primes(n)])
    
    def contain_prime_factors(self, n: int) -> array.array:
        return array.array('Q', [num for num in self.contain_primes(n) if n % num == 0])
    
    def collect_semi_primes(self, n: int) -> Generator:
        primes, not_primes = self.contain_primes(n), self.contain_not_primes(n)
        yield from (num for num in not_primes for i in range(len(primes)) for k in range(i+1) if num == primes[i] * primes[k])

if __name__ == '__main__':
    test_one = Primes()
    array_test_primes = test_one.contain_primes(91)
    print(*array_test_primes)
    array_test_not_primes = test_one.contain_not_primes(91)
    print(*array_test_not_primes)
    array_test_factors = test_one.contain_prime_factors(91)
    print(*array_test_factors)
    
    