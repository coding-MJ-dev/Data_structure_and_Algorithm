# 11. Container With Most Water
class Solution:
    def maxArea(self, h: List[int]) -> int:
        area = 0
        l, r = 0, len(h) - 1

        while l < r:
            curArea = min(h[l], h[r]) * (r - l)
            area = max(area, curArea)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1

        return area
