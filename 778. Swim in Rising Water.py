# 778. Swim in Rising Water


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = grid[0][0]
        rows, cols = len(grid), len(grid[0])
        visit = set()

        hp = []
        heappush(hp, (t, 0, 0))
        visit = set()
        visit.add((0, 0))

        while hp:
            t, r1, c1 = heappop(hp)
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r2, c2 = r1 + dr, c1 + dc
                if 0 <= r2 < rows and 0 <= c2 < cols and (r2, c2) not in visit:
                    if r2 == rows - 1 and c2 == cols - 1:
                        t = max(t, grid[rows - 1][cols - 1])
                        return t
                    visit.add((r2, c2))
                    heappush(hp, (max(t, grid[r2][c2]), r2, c2))

        return t
