# 1049. Last Stone Weight II


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mod = set()
        mod.add(0)
        for stone in stones:
            newMod = set()
            for i in mod:
                newMod.add(i + stone)
                newMod.add(abs(i - stone))
            mod = newMod

        return min(mod)
