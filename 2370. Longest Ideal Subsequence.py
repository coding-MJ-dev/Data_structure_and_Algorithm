# 2370. Longest Ideal Subsequence


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            val = ord(c) - ord('a')
            l = max(0, val - k)
            r = min(25, val + k)
            dp[val] = max(dp[val], max(dp[l:r+1])+ 1)
        return max(dp)


        # dp = [0] * 128
        # ans = 0
        # for c in s:
        #     idx = ord(c)
        #     dp[idx] = max(dp[idx - k: idx + k+1]) + 1
        #     ans = max(dp[idx], ans)
        # return ans