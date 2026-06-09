class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Array for numbers strictly less than n (indices 0 to n-1)
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                # Corrected to a single '=' for assignment
                for j in range(i * i, n, i):
                    primes[j] = False
                    
        return sum(primes)