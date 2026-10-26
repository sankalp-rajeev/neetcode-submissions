class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in results:
                results[sortedWord] = []
            results[sortedWord].append(word)
            
        return list(results.values())