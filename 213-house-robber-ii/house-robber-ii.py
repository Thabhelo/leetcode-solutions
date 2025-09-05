class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            prev2 = 0  # best up to i-2
            prev1 = 0  # best up to i-1
            for x in arr:
                cur = max(prev1, prev2 + x)
                prev2, prev1 = prev1, cur
            return prev1

        # Case A: use houses [1..n-1] (skip first)
        # Case B: use houses [0..n-2] (skip last)
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))