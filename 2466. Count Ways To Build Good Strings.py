# 2466. Count Ways To Build Good Strings

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(len(dp)):
            if i - zero >= 0:
                dp[i] += dp[i-zero]  % ((10**9) + 7)
            if i - one >= 0:
                dp[i] += dp[i-one]  % ((10**9) + 7)
        
        return sum(dp[-(high-low +1):]) % ((10**9) + 7)