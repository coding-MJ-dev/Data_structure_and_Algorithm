# 256. Paint House

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0, 0, 0]

        for c in costs:
            dp0 = c[0] + min(dp[1], dp[2])
            dp1 = c[1] + min(dp[0], dp[2])
            dp2 = c[2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
        
        return min(dp)
