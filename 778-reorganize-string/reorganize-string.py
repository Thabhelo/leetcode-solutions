class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        char_counts = Counter(s)
        max_freq = max(char_counts.values())
        
        # If the most frequent character appears more than half the length of s, reorganization is impossible
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Step 2: Sort characters by frequency in descending order
        sorted_chars = sorted(char_counts.items(), key=lambda x: -x[1])
        print(sorted_chars)
        # Step 3: Flatten sorted characters by frequency order
        sorted_s = []
        for char, count in sorted_chars:
            sorted_s.extend([char] * count)
        
        # Step 4: Split the characters into two halves for alternation
        mid = (len(sorted_s) + 1) // 2
        left, right = sorted_s[:mid], sorted_s[mid:]
        
        # Step 5: Merge two halves in alternating order
        result = []
        for i in range(len(right)):
            result.append(left[i])
            result.append(right[i])
        
        # Append the last element if left has an extra character
        if len(left) > len(right):
            result.append(left[-1])
        
        return ''.join(result)
