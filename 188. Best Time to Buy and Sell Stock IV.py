# 188. Best Time to Buy and Sell Stock IV


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in range(k + 1)]

        for i in range(1, k + 1):
            buy = -prices[0]
            for j, n in enumerate(prices):
                if j > 0:
                    dp[i][j] = max(dp[i][j - 1], n + buy)
                buy = max(buy, dp[i - 1][j] - n)
        # print(dp)
        return dp[-1][-1]
