class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0  # F(0), F(1 - before seeing any nums)
        for x in nums:
            cur = max(prev1, prev2 + x)
            prev2, prev1 = prev1, cur
        return prev1