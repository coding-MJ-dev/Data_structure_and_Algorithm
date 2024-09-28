# 694. Number of Distinct Islands


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, cur, set_r, set_c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                cur.add((set_r - r, set_c - c))
                grid[r][c] = 0
                dfs(r + 1, c, cur, set_r, set_c)
                dfs(r - 1, c, cur, set_r, set_c)
                dfs(r, c + 1, cur, set_r, set_c)
                dfs(r, c - 1, cur, set_r, set_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur = set()
                    dfs(r, c, cur, r, c)
                    islands.add(tuple(cur))

        return len(islands)
