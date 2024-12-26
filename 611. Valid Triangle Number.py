# 611. Valid Triangle Number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for r in range(2, len(nums)):
            l = 0
            m = r - 1
            while l < m:
                if nums[l] + nums[m] > nums[r]:
                    ans += m - l
                    m -= 1
                else:
                    l += 1
        return ans
