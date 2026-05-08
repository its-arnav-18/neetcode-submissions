class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        trp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(trp))
        return [list(i) for i in res]