class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]         # Moves 1 step
            fast = nums[nums[fast]]   # Moves 2 steps
            if slow == fast:
                break
                
        # Phase 2: Finding the entrance to the cycle (the duplicate)
        slow = nums[0]                # Reset slow to the beginning
        while slow != fast:
            slow = nums[slow]         # Both move 1 step now
            fast = nums[fast]
            
        return slow