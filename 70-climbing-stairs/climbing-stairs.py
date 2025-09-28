class Solution:
    def climbStairs(self, n: int) -> int:
        return sum(math.comb(n-k, k) for k in range(n))