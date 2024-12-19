# 934. Shortest Bridge
# O(n2) / O(n2)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = cols = len(grid)
        islands = []

        def dfs(i: int, j: int):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in path:
                return
            
            path.add((i, j))
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        visit = set()
        for i in range(n):
            for j in range(n):
                
                if grid[i][j] == 1:
                    path = set()
                    dfs(i, j) 
                    islands.append(path)
        
        q = deque()
        visit = set()
        for r, c in islands[0]: # add start point
            q.append((r, c, 0)) # row, col, dist
            # visit.add((r,c))

        while q:
            # print(q)
            r, c, dist = q.popleft()
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                i = r + dr
                j = c + dc
                if 0<= i < n and 0 <= j < n and (i, j) not in visit:
                    if (i, j) in islands[1]:
                        return dist
                    q.append((i, j, dist + 1))
        
