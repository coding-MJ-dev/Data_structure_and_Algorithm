# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        numSum = sum(nums)
        curSum = 0

        for i in range(len(nums)):
            if (numSum - nums[i]) / 2 == curSum:
                return i
            curSum += nums[i]

        return -1
