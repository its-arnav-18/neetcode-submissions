class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        k = 0
        for i in range(len(s)):
            if k < len(t) and s[i] == t[k]:
                k += 1

        return len(t) - k