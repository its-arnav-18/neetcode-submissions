class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0

        for last in range(1,len(nums)):
            if nums[last] != nums[start]:
                start+=1
                nums[start] = nums[last]
            
        return start +1
