class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in output:
                output[sorted_word].append(word)
            else:
                output[sorted_word] = [word]
        return list(output.values())

