class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      n=len(nums)
      for i in range(n):
        lsum=rsum=0
        for l in range(i):
            lsum+=nums[l]
        for r in range(i+1,n):
            rsum+=nums[r]
        if lsum==rsum:
            return i
      return -1