# 2370. Longest Ideal Subsequence


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        ans = 0
        for c in s:
            idx = ord(c)
            dp[idx] = max(dp[idx - k: idx + k+1]) + 1
            ans = max(dp[idx], ans)
        return ans