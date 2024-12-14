# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # if nums[start]
        return [start, end-1]