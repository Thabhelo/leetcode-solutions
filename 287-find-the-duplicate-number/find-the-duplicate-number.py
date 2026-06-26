class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p = 0
        for num in nums:
            k = p >> num-1
            if k & 1 == 1:
                return num
            k = k | 1
            k = k << num - 1
            p = p | k   