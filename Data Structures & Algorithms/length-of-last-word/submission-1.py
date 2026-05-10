class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        return len(sp[-1])
