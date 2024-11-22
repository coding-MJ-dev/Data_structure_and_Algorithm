# 926. Flip String to Monotone Increasing
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
            else:
                ans = min(ones, ans + 1)
        return ans


