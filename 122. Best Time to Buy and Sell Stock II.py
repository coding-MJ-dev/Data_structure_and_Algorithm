# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range (1, len(prices)):
            if prices[i] > prices [i-1]:
                profit += prices[i] - prices [i-1] 
        return profit










        # dp = {}

        # def dfs(i, have_stock):
        #     if i == len(prices):
        #         return 0
        #     if (i, have_stock) in dp:
        #         return dp[(i, have_stock)]
            
        #     if have_stock: 
        #         dp[(i, have_stock)] = max(dfs(i+1, have_stock), dfs(i+1, not have_stock) + prices[i])
        #     else:
        #         dp[(i, have_stock)] = max(dfs(i+1, not have_stock) - prices[i], dfs(i+1, have_stock))
            
        #     return dp[(i, have_stock)]
        
        # return dfs(0, False)