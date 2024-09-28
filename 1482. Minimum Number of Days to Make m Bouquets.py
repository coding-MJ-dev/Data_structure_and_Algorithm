# 1482. Minimum Number of Days to Make m Bouquets


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 0, max(bloomDay)
        ans = r + 1

        def can_make(mid):
            flower = 0
            bouquet = 0
            for n in bloomDay:
                if n <= mid:
                    flower += 1
                    if flower == k:
                        bouquet += 1
                        flower = 0
                else:
                    flower = 0
                if bouquet == m:
                    return True
            return False

        while l <= r:
            mid = l + (r - l) // 2
            # print(mid, can_make(mid))

            if can_make(mid):
                ans = min(ans, mid)
                r = mid - 1

            else:
                l = mid + 1

        return ans if ans != max(bloomDay) + 1 else -1
