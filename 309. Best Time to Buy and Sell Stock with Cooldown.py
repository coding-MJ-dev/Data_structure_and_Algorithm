# 309. Best Time to Buy and Sell Stock with Cooldown


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_buy, pre_sell, buy, sell = -prices[0], 0, 0, 0

        for n in prices:
            buy = max(pre_sell - n, pre_buy)
            pre_buy = buy
            pre_sell = sell
            sell = max(n + buy, sell)
            # print(pre_buy, pre_sell, buy, sell)
        return sell
