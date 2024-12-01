class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        # Sort by frequency (descending) and lexicographical order (ascending)
        sorted_words = sorted(count.keys(), key=lambda x: (-count[x], x))

        # Return the top k frequent words
        return sorted_words[:k]


        
