# 802. Find Eventual Safe States


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #n(n+e+nlogn) / n(n+e)

        adj = defaultdict(list)
        indegree = [0] * len(graph)
        for i in range(len(graph)):
            for n in graph[i]:
                adj[n].append(i)
                indegree[i] += 1
        
        q = deque()
        for i, n in enumerate(indegree):
            if n == 0:
                q.append(i)
        
        ans = []
        while q:
            n = q.popleft()
            ans.append(n)
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return sorted(ans)


























        # n = len(graph)
        # indegree = [0] * n # 이 노드에서 출발하는 화살표는 몇 개 인가?
        # adj = defaultdict(list) # 해당 노드로 도착할 수 있는 노드/해당 노드를 향해 화살표를 뻗은 노드
        
        # for i in range(n):
        #     for node in graph[i]:
        #         adj[node].append(i)
        #         indegree[i] += 1
        
        # q = deque() 
        # for i in range(n): # add terminate/leaf node 
        #     if indegree[i] == 0:
        #         q.append(i)

        # safe = [False] * n
        # ans = []
        # while q:
        #     node = q.popleft()
        #     safe[node] = True
        #     ans.append(node)

        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)
        
        # return sorted(ans)
