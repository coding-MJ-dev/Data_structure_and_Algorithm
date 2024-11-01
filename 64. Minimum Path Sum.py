# 64. Minimum Path Sum


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if c == cols - 1 and r == rows - 1:
                    continue
                if c == cols - 1 and r != rows - 1:
                    grid[r][c] = grid[r + 1][c] + grid[r][c]
                elif c != cols - 1 and r == rows - 1:
                    grid[r][c] = grid[r][c + 1] + grid[r][c]
                else:
                    grid[r][c] = min(grid[r + 1][c], grid[r][c + 1]) + grid[r][c]

        return grid[0][0]
