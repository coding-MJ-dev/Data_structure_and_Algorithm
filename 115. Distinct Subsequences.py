# 115. Distinct Subsequences


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for c in s:
            for i in range(len(t), 0, -1):
                if t[i - 1] == c:
                    dp[i] = dp[i - 1] + dp[i]
        # print(dp)
        return dp[-1]
