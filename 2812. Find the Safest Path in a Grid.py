# 2812. Find the Safest Path in a Grid


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        n = len(grid)
        dp = [[-1] * n for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        dist = 0
        visit = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visit:
                    continue
                visit.add((r, c))
                dp[r][c] = dist
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    i, j = dr + r, dc + c
                    if i < 0 or j < 0 or i == n or j == n or (i, j) in visit:
                        continue
                    q.append((i, j))
            dist += 1
        # print(dp)

        hq = [(-dp[0][0], 0, 0)]
        visit = set()
        ans = dp[0][0]
        while hq:
            dist, r, c = heappop(hq)
            if r == n - 1 and c == n - 1:
                return ans
            if (r, c) in visit:
                continue
            visit.add((r, c))
            ans = min(ans, -dist)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                i, j = dr + r, dc + c
                if i < 0 or j < 0 or i == n or j == n or (i, j) in visit:
                    continue
                heappush(hq, (-dp[i][j], i, j))

        return 0
