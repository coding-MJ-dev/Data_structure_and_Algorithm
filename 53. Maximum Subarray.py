# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        curSum = nums[0]
        for n in nums[1:]:
            curSum = max(n, curSum + n)
            res = max(curSum, res)
        return res
