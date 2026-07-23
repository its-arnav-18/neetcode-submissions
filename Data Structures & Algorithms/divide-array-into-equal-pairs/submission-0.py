class Solution:
    def divideArray(self, nums: List[int]) -> bool:
#        count_map = {}
#        for item in items:
#           if item in count_map:
#               count_map[item] += 1  # Increment if already exists
 #           else:
  #              count_map[item] = 1   # Initialize if it's new
   #     
    #    for i in range(len(count_map)):
     #       if count_map[i] % 2 == 0:

        N = len(nums)
        nums.sort()

        i = 0
        while i < N:
            j = i
            while j < N and nums[i] == nums[j]:
                j += 1

            if (j - i) % 2 != 0:
                return False

            i = j

        return True
