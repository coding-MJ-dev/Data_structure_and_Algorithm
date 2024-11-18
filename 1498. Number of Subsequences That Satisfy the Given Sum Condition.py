# 1498. Number of Subsequences That Satisfy the Given Sum Condition

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        ans = 0
        nums.sort()
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += (1 << (r-l)) % mod
                l += 1
            else:
                r -= 1
                
        return ans % mod