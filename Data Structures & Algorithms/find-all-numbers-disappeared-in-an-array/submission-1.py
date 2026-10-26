class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        ret = []
        for i in range(1,len(nums)+1):
            if i not in setNums:
                ret.append(i)
        return ret