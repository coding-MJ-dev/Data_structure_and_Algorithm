# 2439. Minimize Maximum of Array

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        curSum = 0
        target = 0
        ans = 0
        for i, n in enumerate(nums):
            curSum += n
            target = curSum / (i+1)
            ans = max(ceil(target), ans)

        return ans