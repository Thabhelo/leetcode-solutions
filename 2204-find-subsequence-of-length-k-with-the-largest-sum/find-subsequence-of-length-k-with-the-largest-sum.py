class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for _ in range(len(nums) - k):
            min_num = min(nums)
            nums.remove(min_num)
        return nums