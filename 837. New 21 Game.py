# 837. New 21 Game

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        
        windowSum = 0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0
        
        dp = {}
        for i in range(k-1, -1, -1):
            dp[i] = windowSum / maxPts
            windowSum += dp[i]

            removeVal = 0
            if i + maxPts <= n:
                removeVal += dp[i + maxPts] if i + maxPts in dp else 1
            windowSum -= removeVal
        
        return dp[0]