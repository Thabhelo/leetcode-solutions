class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}  # Dictionary to store value and its index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hm:
                return [hm[complement], i]
            hm[nums[i]] = i
