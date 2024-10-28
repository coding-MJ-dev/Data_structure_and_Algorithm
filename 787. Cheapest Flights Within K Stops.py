# 787. Cheapest Flights Within K Stops


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        q = deque()
        q.append((src, 0))
        visit = {}
        visit[src] = 0

        while q and k >= 0:
            for _ in range(len(q)):
                d1, p1 = q.popleft()
                for nei, p2 in adj[d1]:
                    if nei not in visit:
                        visit[nei] = p1 + p2
                    if p1 + p2 <= visit[nei]:
                        visit[nei] = min(visit[nei], p1 + p2)
                        q.append((nei, p1 + p2))
            k -= 1
        # print(visit)
        return visit[dst] if dst in visit else -1
