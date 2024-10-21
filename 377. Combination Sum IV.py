# 377. Combination Sum IV


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(dp)):
            for n in nums:
                if i - n >= 0:
                    dp[i] = dp[i - n] + dp[i]
            # print(dp)

        return dp[-1]
