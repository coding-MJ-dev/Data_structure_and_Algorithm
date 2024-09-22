# 494. Target Sum


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for n in nums:
            newdp = {}
            for k in dp.keys():
                newdp[k + n] = newdp.get(k + n, 0) + dp[k]
                newdp[k - n] = newdp.get(k - n, 0) + dp[k]
            dp = newdp

        return dp[target] if target in dp else 0
