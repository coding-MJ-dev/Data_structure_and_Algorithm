# 2542. Maximum Subsequence Score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(x, y) for x, y in zip(nums1, nums2)]
        pairs.sort(key = lambda x: x[1] * -1)
        ans = 0
        curSum = 0
        hp = []
        for x, y in pairs:
            curSum += x
            heappush(hp, x)
            if len(hp) == k:
                ans = max(ans, curSum * y)
                val = heappop(hp)
                curSum -= val
        
        return ans
