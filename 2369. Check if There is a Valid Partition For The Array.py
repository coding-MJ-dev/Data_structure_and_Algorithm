# 2369. Check if There is a Valid Partition For The Array


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums)+1)
        dp[-1] = True
        for i in range(len(nums)-1, -1, -1):
            if i <= len(nums) -3 and nums[i] == nums[i+1] -1 == nums[i+2] - 2 and dp[i+3]:
                dp[i] = True
            if i <= len(nums) -3 and nums[i] == nums[i+1] == nums[i+2] and dp[i+3]:
                dp[i] = True
            if i <= len(nums) -2 and nums[i] == nums[i+1] and dp[i+2]:
                dp[i] = True
        return dp[0]
        