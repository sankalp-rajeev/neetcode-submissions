class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Input: nums = [1,2,3]
        numSet = set(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in numSet:
                return i
                

        