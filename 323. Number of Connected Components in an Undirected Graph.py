# 323. Number of Connected Components in an Undirected Graph


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        adj = {i: [] for i in range(n)}
        for st, en in edges:
            adj[st].append(en)
            adj[en].append(st)

        visit = set()

        def dfs(i):
            # if i in visit:
            #     return
            visit.add(i)
            for nei in adj[i]:
                if nei in visit:
                    continue
                dfs(nei)

        for i in range(n):
            if i not in visit:
                ans += 1
                dfs(i)

        return ans

        # par = {i:i for i in range(n)}
        # rank = [1] * (n)

        # def find(n):
        #     p = par[n]
        #     while p != par[p]:
        #         par[p] = par[par[p]]
        #         p = par[p]
        #     return p

        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)

        #     if p1 == p2:
        #         return False

        #     else:
        #         if rank[p1] >= rank[p2]:
        #             par[p2] = p1
        #             rank[p1] += 1
        #         else:
        #             par[p1] = p2
        #             rank[p2] += 1
        #         return True

        # for n1, n2 in edges:
        #     union(n1, n2)

        # count = set()
        # for i in par.values():
        #     count.add(find(i))
        # return len(count)
