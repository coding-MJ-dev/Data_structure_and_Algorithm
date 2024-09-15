# 1245. Tree Diameter


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        q = deque()

        prev = None
        q.append((0, prev))
        lastNode = None
        while q:
            for _ in range(len(q)):
                node, prev = q.popleft()
                lastNode = node
                for nei in adj[node]:
                    if nei == prev:
                        continue
                    q.append((nei, node))

        q.append((lastNode, 0))
        maxDist = 0
        visit = set()
        while q:
            # print(q)
            node, dist = q.popleft()
            visit.add(node)
            maxDist = max(maxDist, dist)
            for nei in adj[node]:
                if nei in visit:
                    continue
                q.append((nei, dist + 1))
        return maxDist
