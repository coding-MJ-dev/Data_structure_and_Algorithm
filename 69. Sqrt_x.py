# 69. Sqrt_x


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l <= r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m < x:
                ans = max(m, ans)
                l = m + 1
            else:
                r = m - 1
        return ans
