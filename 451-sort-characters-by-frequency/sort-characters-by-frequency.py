class Solution:
    def frequencySort(self, s: str) -> str:
        # 1) Count frequencies
        freq = Counter(s)
        
        # 2) Sort by frequency, descending
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        
        # 3) Build the string
        return ''.join([ch * count for ch, count in sorted_chars])