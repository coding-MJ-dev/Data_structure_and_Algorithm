# 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[-1] = 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if j < n - 1:
                    dp[j] = dp[j] + dp[j + 1]

        return dp[0]
