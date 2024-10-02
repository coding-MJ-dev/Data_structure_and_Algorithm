# 417. Pacific Atlantic Water Flow


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        p_dp = [[False] * cols for _ in range(rows)]
        a_dp = [[False] * cols for _ in range(rows)]

        p_visit = set()
        a_visit = set()

        def dfs(i, j, dp, visit):
            dp[i][j] = True
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                r = i + dr
                c = j + dc
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and dp[r][c] == False
                    and heights[r][c] >= heights[i][j]
                ):
                    dfs(r, c, dp, visit)

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dfs(i, j, p_dp, p_visit)
                if i == rows - 1:
                    dfs(i, j, a_dp, a_visit)
                if j == 0:
                    dfs(i, j, p_dp, p_visit)
                if j == cols - 1:
                    dfs(i, j, a_dp, a_visit)

        ans = []
        for i in range(rows):
            for j in range(cols):
                if a_dp[i][j] and p_dp[i][j]:
                    ans.append([i, j])

        return ans
