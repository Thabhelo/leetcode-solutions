import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Count character frequencies
        counts = collections.Counter(s)
        
        # 2. Check for impossibility condition
        # If any character count is greater than (length + 1) // 2, it's impossible.
        max_freq = 0
        for count in counts.values():
            max_freq = max(max_freq, count)
        
        n = len(s)
        if max_freq > (n + 1) // 2:
            return ""
        
        # 3. Build a Max Heap (Priority Queue)
        # Python's heapq is a Min Heap, so we store negative frequencies 
        # to simulate a Max Heap based on frequency.
        pq = []
        for char, freq in counts.items():
            heapq.heappush(pq, (-freq, char))
            
        result = []
        
        # 4. Greedily construct the result string
        # Process two most frequent characters at a time.
        while len(pq) >= 2:
            # Pop the two most frequent characters
            neg_freq1, char1 = heapq.heappop(pq)
            neg_freq2, char2 = heapq.heappop(pq)
            
            # Append them to the result
            result.append(char1)
            result.append(char2)
            
            # Decrease their frequencies and push back to the heap if they still remain
            if neg_freq1 + 1 < 0:
                heapq.heappush(pq, (neg_freq1 + 1, char1))
            if neg_freq2 + 1 < 0:
                heapq.heappush(pq, (neg_freq2 + 1, char2))
                
        # 5. Handle the remaining character (if any)
        # If the heap is not empty, it must contain only one element, 
        # and its frequency must be -1 (due to the impossibility check)
        if pq:
            neg_freq, char = heapq.heappop(pq)
            # Since we already checked if max_freq > (n+1)//2, 
            # the only remaining character must have a frequency of 1.
            # (-neg_freq == 1)
            result.append(char)
            
        return "".join(result)