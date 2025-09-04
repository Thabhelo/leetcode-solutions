class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        if len(p) > len(s):
            return []
        
        # Count frequency of characters in p
        p_counter = {}
        for char in p:
            p_counter[char] = p_counter.get(char, 0) + 1

        # Sliding window
        window_counter = {}
        result = []
        window_size = len(p)

        for i in range(window_size):
            window_counter[s[i]] = window_counter.get(s[i], 0) + 1

        # Check if first window is an anagram of p
        if window_counter == p_counter:
            result.append(0)

        # Slide the window
        for i in range(window_size, len(s)):
            # Add new character to window
            new_char = s[i]
            window_counter[new_char] = window_counter.get(new_char, 0) + 1

        # Remove character that's no longer in window
            old_char = s[i - window_size]
            window_counter[old_char] -= 1
            if window_counter[old_char] == 0:
                del window_counter[old_char]

        # Check if current window is an anagram
            if window_counter == p_counter:
                result.append(i - window_size + 1)

        return result

