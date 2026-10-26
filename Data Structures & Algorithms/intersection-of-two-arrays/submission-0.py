class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numS1 = set(nums1)
        numS2 = set(nums2)
        return list(numS1 & numS2)
        
        