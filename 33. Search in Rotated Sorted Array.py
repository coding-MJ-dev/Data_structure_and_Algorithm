# 33. Search in Rotated Sorted Array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else: 
                    r = m - 1
            
        return -1