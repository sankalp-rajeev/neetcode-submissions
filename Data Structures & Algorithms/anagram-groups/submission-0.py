class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in result:
                result[sortedWord] = []
            result[sortedWord].append(word)
        return list(result.values())