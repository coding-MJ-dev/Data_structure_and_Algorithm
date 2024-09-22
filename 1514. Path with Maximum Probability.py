# 1514. Path with Maximum Probability


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        neimap = {i: [] for i in range(n)}
        for i in range(len(succProb)):
            neimap[edges[i][0]].append((-succProb[i], edges[i][1]))
            neimap[edges[i][1]].append((-succProb[i], edges[i][0]))

        visit = set()
        hp = []
        for start in neimap[start_node]:
            heappush(hp, start)
        ans = -1.0

        while hp:
            prob, node = heappop(hp)
            if node == end_node:
                ans = max(-prob, ans)
                return ans
            else:
                visit.add(node)
            for nei_prob, nei in neimap[node]:
                if nei in visit:
                    continue
                heappush(hp, (-nei_prob * prob, nei))
        # print(ans)
        return ans if ans != -1.0 else 0
