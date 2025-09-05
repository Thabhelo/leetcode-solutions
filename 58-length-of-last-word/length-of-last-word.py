class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split()
        return len(splitted[-1])
        
        