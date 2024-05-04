from games import Game
import array
import itertools

class Primes(Game):
    
    def collect_primes(self, n: int) -> iter:
        yield from (i for i in range(2, n+1) if sum(i % k == 0 for k in range(1, int(i**0.5) + 1)) == 1)
    
    def contain_primes(self, n: int) -> array:
        primes = self.collect_primes(n)
        container = array.array('Q')
        while True:
            try: container.append(next(primes))
            except StopIteration: break
        return container
    
    def contain_not_primes(self, n: int) -> array:
        primes = self.contain_primes(n)
        return array.array('Q', [num for num in range(n+1) if num not in primes])
    
    def collect_semi_primes(self, n: int) -> array:
        primes = self.contain_primes(n)
        not_primes = self.contain_not_primes(n)
        
        
        

if __name__ == '__main__':
    test_one = Primes()
    first_value = test_one.collect_primes(100)
    print(next(first_value))
    test_two = Primes()
    array_test_primes = test_two.contain_primes(100)
    print(array_test_primes)
    test_three = Primes()
    array_test_not_primes = test_three.contain_not_primes(100)
    print(array_test_not_primes)
    