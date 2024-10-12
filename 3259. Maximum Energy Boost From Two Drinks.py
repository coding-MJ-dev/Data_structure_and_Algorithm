# 3259. Maximum Energy Boost From Two Drinks


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dp1 = dp2 = 0

        for i in range(len(energyDrinkA)):
            dp1, dp2 = max(dp2, dp1 + energyDrinkA[i]), max(dp1, dp2 + energyDrinkB[i])

        return max(dp1, dp2)
