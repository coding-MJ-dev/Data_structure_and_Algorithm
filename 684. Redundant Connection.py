# 684. Redundant Connection


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {i + 1: i + 1 for i in range(len(edges))}
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            else:
                if rank[p1] >= rank[p2]:
                    par[p2] = p1
                    rank[p1] += 1
                else:
                    par[p1] = p2
                    rank[p2] += 1
                return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []
