# 673. Number of Longest Increasing Subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {i : [1, 1] for i in range(len(nums))} # key: index / value : (LIS, count)
        globalLIS, globalCount = 0, 0

        for i in range(len(nums)-1, -1, -1):
            curLIS, curCount = 1, 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    preLIS, preCount = dp[j]
                    if preLIS + 1 > curLIS:
                        curLIS = preLIS + 1
                        curCount = preCount
                    elif preLIS + 1 == curLIS:
                        curCount += preCount
            dp[i] = [curLIS, curCount]

            if globalLIS < curLIS:
                globalLIS = curLIS
                globalCount = curCount
            elif globalLIS == curLIS:
                globalCount += curCount
        
        return globalCount



##        다른 해결책
        # dp = [1] * len(nums)
        # count = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if dp[j] + 1 > dp[i]:
        #                 dp[i] = dp[j] + 1
        #                 count[i] = count[j]
        #             elif dp[j]+1 == dp[i]:
        #                 count[i] += count[j]

        # lis = max(dp)
        # n_lis = 0

        # for i in range(len(nums)):
        #     if dp[i] == lis:
        #         n_lis += count[i]

        # return n_lis
