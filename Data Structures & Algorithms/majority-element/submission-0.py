class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {} 
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]]+=1
            if dict[nums[i]]>n//2:
                return nums[i]