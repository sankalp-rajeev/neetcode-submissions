class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Input: nums = [1,2,3]
        # numSet = set(nums)
        n = len(nums)
        # for i in range(n+1):
        #     if i not in numSet:
        #         return i
        
        currSum = sum(nums)
        expSum = 0
        for i in range(n+1):
            expSum+=i
        return expSum - currSum
                

        