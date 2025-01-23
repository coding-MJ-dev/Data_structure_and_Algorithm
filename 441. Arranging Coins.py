# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = l + (r - l) // 2
            sum_up = (1 + m) * m / 2
            if sum_up == n:
                return m
            elif sum_up < n: 
                l = m + 1
            else:
                r = m - 1
        return r