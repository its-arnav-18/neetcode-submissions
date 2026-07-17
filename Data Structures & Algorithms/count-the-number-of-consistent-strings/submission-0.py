class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            has_strs = set(word).issubset(set(allowed))
            if has_strs:
                count += 1
        return count