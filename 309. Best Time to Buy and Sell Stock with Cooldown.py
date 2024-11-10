# 309. Best Time to Buy and Sell Stock with Cooldown


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = -prices[0]
        sell = 0
        cooldown = 0

        for n in prices:
            pre_buy = buy
            buy = max(buy, cooldown - n)
            cooldown = max(sell, cooldown)
            sell = n + pre_buy
        
        return max(sell, cooldown)















        # pre_buy, pre_sell, buy, sell = -prices[0], 0, 0, 0

        # for n in prices:
        #     buy = max(pre_sell - n, pre_buy)
        #     pre_buy = buy
        #     pre_sell = sell
        #     sell = max(n + buy, sell)
        #     # print(pre_buy, pre_sell, buy, sell)
        # return sell
