# 3020. Find the Maximum Number of Elements in Subset


from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for n in count:
            if n == 1:
                ans = max(ans, count[n] if count[n] % 2 else count[n] -1)
            else:
                cur = 0
                while n ** 2 in count and count[n] >= 2:
                   cur += 2
                   n = n**2
                cur += 1
                ans = max(cur, ans)
        return ans

