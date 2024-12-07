class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        IsPrime = [True] * n
        IsPrime[0] = IsPrime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if IsPrime[i]:
                for multiple in range(i * i, n, i):
                    IsPrime[multiple] = False
        return sum(IsPrime)  