# 547. Number of Provinces
# O(n2), O(n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1
        
        return ans



        # n = len(isConnected)
        # adj = [[] for _ in range(n)]  # convert adj matrix to adj list
        # for u in range(n):
        #     for v in range(n):
        #         if u != v and isConnected[u][v]:
        #             adj[u].append(v)

        # def dfs(v) -> None:
        #     visited.add(v)
        #     for u in adj[v]:
        #         if u not in visited:
        #             dfs(u)

        # visited = set()
        # count = 0
        # for v in range(n):
        #     if v not in visited:
        #         visited.add(v)
        #         dfs(v)
        #         count += 1

        # return count










# class UF:
#     def __init__(self, n):
#         self.par = [i for i in range(n)]
#         self.rank = [1 for i in range(n)]

#     def find(self, n):
#         par = self.par[n]
#         while par != self.par[par]:
#             par = self.par[par]
#         return par

#     def union(self, n1, n2):
#         p1, p2 = self.find(n1), self.find(n2)
#         if p1 == p2:
#             return False
#         else:
#             if self.rank[p1] >= self.rank[p2]:
#                 self.rank[p1] += 1

#                 self.par[p2] = p1
#             else: 
#                 self.rank[p2] += 1

#                 self.par[p1] = p2
#             return True

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         #union find
#         rows, cols = len(isConnected), len(isConnected[0])
#         uf = UF(len(isConnected))
#         ans = rows
#         for i in range(rows):
#             for j in range(cols):
#                 if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
#                     uf.union(i, j)
#                     ans -= 1

        
#         # print(uf.par, uf.rank)

#         return ans