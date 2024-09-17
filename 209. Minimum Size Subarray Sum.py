# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        if sum(nums) < t:
            return 0
        i, curSum = 0, 0
        ans = len(nums)
        for j, n in enumerate(nums):
            curSum += n

            while curSum >= t:
                ans = min(ans, j - i + 1)
                curSum -= nums[i]
                i += 1

        return ans
