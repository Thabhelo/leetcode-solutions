from math import floor, ceil
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0
        if n <= 0:
            return False
        return math.floor(math.log2(n)) == math.ceil(math.log2(n))

        