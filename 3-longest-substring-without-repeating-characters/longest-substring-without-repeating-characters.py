class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen stores { character: last_index }
        seen = {}
        start = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If char was seen and is inside the current window, 
            # jump the start pointer to one position past the previous occurrence
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            
            # Record/update the character's most recent index
            seen[char] = right
            
            # Calculate current window size and update global max
            max_length = max(max_length, right - start + 1)
            
        return max_length
