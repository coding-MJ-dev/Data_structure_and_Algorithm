# 743. Network Delay Time

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra!!!!!!!!!
        adj = defaultdict(list)
        for s, d, w in times:
            adj[s].append((d, w))

        visit = set()
        q = [(0, k)]
        result = 0
        while q:
            d1, n1 = heapq.heappop(q)
            if n1 in visit:
                continue
            visit.add(n1)
            result = max(result, d1)
            for n2, d2 in adj[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(q, (d2 + d1, n2))

        return result if len(visit) == n else -1
