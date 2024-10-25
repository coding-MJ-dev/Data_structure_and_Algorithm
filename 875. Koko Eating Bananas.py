# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat(m):
            hours = 0
            for p in piles:
                hours += ceil(p / m)
            return hours

        ans = max(piles)
        while l <= r:
            m = l + (r - l) // 2

            if eat(m) <= h:
                ans = min(m, ans)
                r = m - 1

            else:
                l = m + 1
        return ans
