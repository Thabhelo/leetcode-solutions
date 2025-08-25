class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        left = n - m
        right = n - 1

        min_val = float('inf')
        max_val = float('-inf')
        result = float('-inf')

        while left >= 0:
            min_val = min(min_val, nums[right])
            max_val = max(max_val, nums[right])
            result = max(result, nums[left] * min_val, nums[left] * max_val)
            left -= 1
            right -= 1

        return result