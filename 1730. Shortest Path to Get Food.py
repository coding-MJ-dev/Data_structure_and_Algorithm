# 1730. Shortest Path to Get Food


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    q.append((0, r, c))
                    grid[r][c] = "X"
                    break

        while q:
            step, r1, c1 = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r2, c2 = r1 + dr, c1 + dc
                if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] != "X":
                    if grid[r2][c2] == "#":
                        return step + 1
                    grid[r2][c2] = "X"
                    q.append((step + 1, r2, c2))

        return -1
