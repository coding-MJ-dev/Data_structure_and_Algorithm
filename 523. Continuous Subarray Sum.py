# 523. Continuous Subarray Sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0 : -1}
        curSum = 0
        for i, n in enumerate(nums):
            curSum = (curSum + n) % k
            if curSum in seen:
                if i - seen[curSum] > 1:
                    return True
            else:
                seen[curSum] = i
        return False
