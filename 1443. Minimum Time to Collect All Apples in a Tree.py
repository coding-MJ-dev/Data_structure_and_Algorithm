# 1443. Minimum Time to Collect All Apples in a Tree


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(node,prev):
            time = 0
            for child in adj[node]:
                if child == prev:
                    continue
                child_time = dfs(child, node)
                if child_time or hasApple[child]:
                    time += child_time + 2
            # print(node, time)
            return time
        
        return dfs(0,-1)
            