class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # reorder the numbers
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # Swap nums[i] to  correct position
        # first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # if all numbers are in the correct positions, return n + 1
        return n + 1