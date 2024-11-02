# 2300. Successful Pairs of Spells and Potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for s in spells:
            target = success / s
            l, r = 0, len(potions)
            while l < r:
                m = l + (r - l) // 2

                if potions[m] >= target:
                    r = m
                else:
                    l = m + 1
            ans.append(len(potions) - l)

        return ans
