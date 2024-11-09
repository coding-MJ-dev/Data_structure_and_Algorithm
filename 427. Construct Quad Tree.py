# 427. Construct Quad Tree

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def dfs(r, c, n):
            isSame = True
            val = grid[r][c]
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != val:
                        isSame = False
                        break
            if isSame:
                res = Node(val, True, None, None, None, None)
            else:
                n = n // 2
                res = Node(-1, False, dfs(r, c, n), dfs(r, c+n, n), dfs(r+n, c, n), dfs(r+n, c+n, n))
            return res
        return dfs(0, 0, n)



