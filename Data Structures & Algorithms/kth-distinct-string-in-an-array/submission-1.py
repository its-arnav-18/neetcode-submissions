class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for i in arr:
            seen[i] = seen.get(i,0) + 1

        count = 0

        for key, value in seen.items():
            if value == 1:
                count += 1
                if count == k:
                    return key
        return ""
