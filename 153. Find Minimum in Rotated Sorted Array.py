# 153. Find Minimum in Rotated Sorted Array


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = 5001
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            ans = min(nums[m], ans)
            if nums[l] <= nums[m]:
                if nums[l] <= nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                r = m - 1
        return ans
