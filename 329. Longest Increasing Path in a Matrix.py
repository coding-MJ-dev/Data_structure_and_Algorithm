# 329. Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            if r < 0  or c < 0 or r == rows or c == cols or matrix[r][c] <= prevVal:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
        
            res = 1
            res = max(res, dfs(r+1, c, matrix[r][c])+1)
            res = max(res, dfs(r, c+1, matrix[r][c])+1)
            res = max(res, dfs(r-1, c, matrix[r][c])+1)
            res = max(res, dfs(r, c-1, matrix[r][c])+1)

            dp[(r, c)] = res
            return dp[(r, c)]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(dp.values())
