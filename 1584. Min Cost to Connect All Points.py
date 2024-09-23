# 1584. Min Cost to Connect All Points


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hp = []
        res = 0
        # heappush(hp, (0,))
        x1, y1 = points[0]
        for j in range(1, len(points)):
            x2, y2 = points[j]
            heappush(hp, (abs(x2 - x1) + abs(y2 - y1), j))
        visit = set()
        visit.add(0)

        while hp:
            dist, node = heappop(hp)
            if node in visit:
                continue
            visit.add(node)
            x1, y1 = points[node]
            res += dist
            if len(visit) == len(points):
                return res
            for j in range(len(points)):
                if j in visit:
                    continue
                x2, y2 = points[j]
                heappush(hp, (abs(x2 - x1) + abs(y2 - y1), j))

        return res
