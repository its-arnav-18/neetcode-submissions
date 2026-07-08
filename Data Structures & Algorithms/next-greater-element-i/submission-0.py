class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:
            pos = nums2.index(x)
            found = False

            for k in range(pos + 1, len(nums2)):
                if nums2[k] > x:
                    ans.append(nums2[k])
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans
                    