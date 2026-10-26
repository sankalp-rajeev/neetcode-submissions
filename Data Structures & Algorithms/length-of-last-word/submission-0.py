class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s.split().pop())
        return length