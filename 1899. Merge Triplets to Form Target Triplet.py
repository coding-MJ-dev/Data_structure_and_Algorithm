# 1899. Merge Triplets to Form Target Triplet


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        aMax = -1
        bMax = -1
        cMax = -1

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            aMax = max(a, aMax)
            bMax = max(b, bMax)
            cMax = max(c, cMax)

        return [aMax, bMax, cMax] == target
