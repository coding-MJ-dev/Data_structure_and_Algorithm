# 474. Ones and Zeroes


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m is 0 , n is 1
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            for i in range(len(dp) - 1, ones - 1, -1):
                for j in range(len(dp[0]) - 1, zeros - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeros] + 1)
            # print(dp)
        return dp[-1][-1]
