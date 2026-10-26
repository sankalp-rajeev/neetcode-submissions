class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                result+=''.join(c)
        return result == result[::-1]
        


        
        