# 746. Min Cost Climbing Stairs


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = cost[0]
        dp2 = cost[1]

        for n in cost[2:]:
            temp = min(dp1 + n, dp2 + n)
            dp1 = dp2
            dp2 = temp
            # print(dp1, dp2, n)

        return min(dp1, dp2)
