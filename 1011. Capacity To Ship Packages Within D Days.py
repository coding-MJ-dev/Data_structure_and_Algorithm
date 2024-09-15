# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def check(m):
            cur = 0
            day = 1
            for w in weights:
                if cur + w > m:
                    day += 1
                    cur = 0
                cur += w
            return day

        while l < r:
            m = l + (r - l) // 2

            if check(m) > days:
                l = m + 1
            else:
                r = m

        return l
