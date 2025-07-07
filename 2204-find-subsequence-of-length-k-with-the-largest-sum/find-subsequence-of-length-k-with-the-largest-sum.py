class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for _ in range(len(nums) - k):
            nums.remove(min(nums))
        return nums