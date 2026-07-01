class Solution:
    def maxDifference(self, s: str) -> int:

        max_odd=0
        min_even=float('inf')
        for i in range(len(s)):
            count=0
            for j in range(len(s)):


                if s[i]==s[j]:
                    count+=1

            if count%2==1:
                max_odd=max(max_odd,count)

            else:
                min_even=min(min_even,count)

        return max_odd-min_even 