# 91. Decode Ways


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        if s[0] == "0":
            return 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
            if i < len(s) - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]
