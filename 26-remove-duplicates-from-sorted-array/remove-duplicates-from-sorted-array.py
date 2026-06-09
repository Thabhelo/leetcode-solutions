class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        k = 1  # since first element is trivially unique
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # Check if nums[i] is a new unique element
                nums[k] = nums[i]       # Place it in the k-th position
                k += 1                  # Increment k
        return k
            