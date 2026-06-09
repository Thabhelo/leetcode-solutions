class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(list(set(nums)))
        result = unique_nums + (["_"] * (len(nums) - len(unique_nums)))
        nums[:] = result
        return len(unique_nums)