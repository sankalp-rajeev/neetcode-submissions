class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l<=r:
            b = r-l
            h = min(heights[l],heights[r])
            currArea = b*h
            maxArea = max(currArea,maxArea)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
            
        