# 1631. Path With Minimum Effort


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        heap = [(0, 0, 0)]  # max_diff, r, c
        visit = set()

        while heap:
            diff, r, c = heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return diff
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i = r + dr
                j = c + dc
                if 0 <= i < rows and 0 <= j < cols and (i, j) not in visit:
                    gap = abs(heights[r][c] - heights[i][j])
                    heappush(heap, (max(diff, gap), i, j))
        return -1
