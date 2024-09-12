# 1481. Least Number of Unique Integers after K Removals

from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        # someone has better idea
        freq = Counter(arr)
        minHeap = list(freq.values())
        heapq.heapify(minHeap)

        while minHeap and k >= minHeap[0]:
            k -= heapq.heappop(minHeap)

        return len(minHeap)


sol = Solution()
print(sol.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))


# MY solution
# seen = Counter(arr)
# hp = [(v, n) for n, v in seen.items()]
# heapify(hp)

# while k and hp:
#     v, n = heappop(hp)
#     if v <= k:
#         k -= v
#     else:
#         v -= k
#         k = 0
#         heappush(hp, (v, n))
#         break
# return len(hp)
