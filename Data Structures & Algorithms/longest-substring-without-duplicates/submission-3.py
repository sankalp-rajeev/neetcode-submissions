class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = ""
        # result = ""
        # for c in s:
        #     if c not in seen:
        #         seen+=c
        #     else:
        #         break
        # return len(seen)
        
        seen = set()
        l=0
        maxLength = 0
        n = len(s)
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            length = r-l+1
            maxLength = max(maxLength,length)
            seen.add(s[r])
            
        return maxLength