from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        window = {}

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if (
                    s[left] in count_t
                    and window[s[left]] < count_t[s[left]]
                ):
                    have -= 1

                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("inf") else ""