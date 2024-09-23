# 322. Coin Change


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(len(dp)):
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
            # print(dp)

        return dp[-1] if dp[-1] != amount + 1 else -1
