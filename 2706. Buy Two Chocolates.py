# 2706. Buy Two Chocolates


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        return (
            money
            if money - (prices[0] + prices[1]) < 0
            else money - (prices[0] + prices[1])
        )
