# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation.
#
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:
# """

class Solution:
    
    def findPeak(self, mountainArr):
        left, right = 0, mountainArr.length() - 1

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        return left

    def binarySearchAsc(self, mountainArr, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def binarySearchDesc(self, mountainArr, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findPeak(mountainArr)

        # Search in ascending part
        left_result = self.binarySearchAsc(
            mountainArr, target, 0, peak
        )

        if left_result != -1:
            return left_result

        # Search in descending part
        return self.binarySearchDesc(
            mountainArr,
            target,
            peak + 1,
            mountainArr.length() - 1
        )