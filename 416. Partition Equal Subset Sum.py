# 416. Partition Equal Subset Sum


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [0] * (target + 1)
        dp[0] = 1

        nums.sort()
        for n in nums:
            for i in range(len(dp) - 1, n - 1, -1):
                if i >= 0 and dp[i - n] == 1:
                    dp[i] = 1
                    if dp[-1] == 1:
                        return True
        return True if dp[-1] == True else False
