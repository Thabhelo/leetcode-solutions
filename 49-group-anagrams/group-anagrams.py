class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in output:
                output[sorted_word] = []
            output[sorted_word].append(word)
        return list(output.values())

