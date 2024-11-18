# 2407. Longest Increasing Subsequence II


class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n * 2
    
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i*2], self.tree[i*2 + 1])       


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        seg = SEG(max(nums))
        ans = 0
        for n in nums:
            n -= 1
            preMax = seg.query(max(0, n-k), n)
            ans = max(ans, preMax + 1)
            seg.update(n, preMax+1)
        return ans