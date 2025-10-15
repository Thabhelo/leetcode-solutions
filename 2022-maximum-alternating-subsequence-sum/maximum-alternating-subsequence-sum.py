class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0  # best sum ending with a '+'
        odd = 0   # best sum ending with a '-'
        for num in nums:
            new_even = max(even, odd + num)
            new_odd  = max(odd,  even - num)
            even, odd = new_even, new_odd
        return even

