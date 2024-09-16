# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(dp) - 1, -1, -1):
            for j in range(i, len(dp)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)
