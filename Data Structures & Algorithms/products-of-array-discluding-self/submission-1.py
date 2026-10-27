class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lMul,rMul = 1,1
        n = len(nums)
        lArr = [0]*n
        rArr = [0]*n
        for i in range(n):
            j = -i-1
            lArr[i]=lMul
            rArr[j] = rMul
            lMul*=nums[i]
            rMul*=nums[j]
        result = []
        for i in range(n):
            result.append(lArr[i]*rArr[i])
        return result
        

        