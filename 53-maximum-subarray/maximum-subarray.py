class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm, linear time
        cur = max_sum = nums[0]
        for x in nums[1:]:
            cur = max(cur + x, x)
            max_sum = max(cur, max_sum)
        return max_sum
