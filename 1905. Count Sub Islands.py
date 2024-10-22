# 1905. Count Sub Islands


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        grid3 = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 1 and grid2[r][c] == 1:
                    grid3[r][c] = 1

        def dfs(r, c, grid, cur):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                cur.add((r, c))
                grid[r][c] = 0
                for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    i, j = r + dr, c + dc
                    dfs(i, j, grid, cur)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid3[r][c] == 1 and grid2[r][c] == 1:
                    cur1 = set()
                    cur2 = set()
                    dfs(r, c, grid2, cur1)
                    dfs(r, c, grid3, cur2)
                    if cur1 == cur2:
                        count += 1
        return count
