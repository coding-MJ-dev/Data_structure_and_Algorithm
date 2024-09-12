# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                pre_temp, pre_i = stack.pop()
                dp[pre_i] = i - pre_i
            stack.append((temp, i))

        return dp
