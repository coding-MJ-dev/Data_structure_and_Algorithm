# 918. Maximum Sum Circular Subarray


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        numSum = sum(nums)
        globalmin = float("inf")
        globalmax = -float("inf")
        curmin = float("inf")
        curmax = -float("inf")

        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            globalmax = max(globalmax, curmax)
            globalmin = min(globalmin, curmin)

        return max(globalmax, numSum - globalmin) if globalmax > 0 else globalmax
