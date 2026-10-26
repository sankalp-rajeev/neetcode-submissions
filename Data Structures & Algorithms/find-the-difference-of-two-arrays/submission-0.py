class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)
        diff1 = num1-num2
        diff2=num2-num1
        return[list(diff1),list(diff2)]