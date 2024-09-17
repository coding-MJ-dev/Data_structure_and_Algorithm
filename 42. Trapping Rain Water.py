# 42. Trapping Rain Water
class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        water = 0
        cur_l = h[l]
        cur_r = h[r]
        while l < r:
            if h[l] <= h[r]:
                water += min(cur_l, cur_r) - h[l]
                l += 1
                cur_l = max(cur_l, h[l])
            else:
                water += min(cur_l, cur_r) - h[r]
                r -= 1
                cur_r = max(cur_r, h[r])
        return water
