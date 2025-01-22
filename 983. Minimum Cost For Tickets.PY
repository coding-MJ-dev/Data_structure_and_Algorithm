# 983. Minimum Cost For Tickets


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days = set(days)
        for i in range(len(dp)):
            if i in days:
                dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]






        # dp = [costs[-1] * days[-1]] * (days[-1] + 1)
        # dp[0] = 0
        # for i in range(1, len(dp)):
        #     if i not in days:
        #         dp[i] = dp[i - 1]
        #     else:
        #         for j, d in enumerate([1, 7, 30]):
        #             if i - d <= 0:
        #                 dp[i] = min(dp[i], dp[0] + costs[j])
        #             else:
        #                 dp[i] = min(dp[i], dp[i - d] + costs[j])
        #     # print(dp)
        # return dp[-1]
