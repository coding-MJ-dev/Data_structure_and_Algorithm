# 540. Single Element in a Sorted Array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            
            if (m == 0 or nums[m] != nums[m-1]) and (m == len(nums)-1 or nums[m] != nums[m+1]):
                return nums[m]

            left = m + 1 if m+1 < len(nums) and nums[m] == nums[m+1] else m

            if left % 2 == 0:
                r = m -1
            else:
                l = m +1
        return nums[l]