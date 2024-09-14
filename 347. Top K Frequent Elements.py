# 347. Top K Frequent Elements


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for c in nums:
            seen[c] = seen.get(c, 0) + 1

        freq = list(seen.items())
        freq.sort(key=lambda x: x[1] * -1)

        ans = [i[0] for i in freq]
        return ans[:k]
