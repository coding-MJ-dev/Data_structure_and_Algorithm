# 560. Subarray Sum Equals K


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {}
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum == k:
                res += 1
            if curSum - k in seen:
                res += seen[curSum - k]
            seen[curSum] = seen.get(curSum, 0) + 1

        return res
