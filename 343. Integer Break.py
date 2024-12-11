# 343. Integer Break

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {0:0, 1:1}

        for num in range(2, n+1):
            val = 0 if num == n else num
            for i in range(1, num):
                val = max(val, dp[i] * dp[num-i])
            dp[num] = val
        
        return dp[n]
