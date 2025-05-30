class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
    
        count = Counter(words)
        result = 0
        center_used = False
        
        for word in count:
            if word[0] == word[1]:  # Palindromic word like "aa", "bb"
                pairs = count[word] // 2
                result += pairs * 4  # Each pair contributes 4 characters
                
                # Use one leftover in center if available and not used yet
                if count[word] % 2 == 1 and not center_used:
                    result += 2
                    center_used = True
                    
            else:  # Non-palindromic word like "ab"
                reverse_word = word[1] + word[0]  # "ba" for "ab"
                
                if reverse_word in count and count[word] > 0:
                    pairs = min(count[word], count[reverse_word])
                    result += pairs * 4  # Each pair contributes 4 characters
                    
                    # Mark as processed to avoid double counting
                    count[word] = 0
                    count[reverse_word] = 0
        
        return result