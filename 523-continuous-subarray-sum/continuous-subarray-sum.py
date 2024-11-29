class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapp = {0: -1}  # Dictionary to store remainder and its first occurrence index
        preSum = 0
        
        for index, num in enumerate(nums):
            preSum += num
            remainder = preSum % k
            
            if remainder in mapp:
                # Check if the subarray length is at least 2
                if index - mapp[remainder] > 1:
                    return True
            else:
                # Store the first occurrence of the remainder
                mapp[remainder] = index
        
        return False
