class Solution:
    def countElements(self, arr: List[int]) -> int:
        ct = 0
        for i in arr:
            if i+1 in arr:
                ct+=1
        return ct
        