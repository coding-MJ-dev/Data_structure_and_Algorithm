# 221. Maximal Square


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                matrix[r][c] = int(matrix[r][c])
                if matrix[r][c] == 0:
                    continue

                if r == rows - 1 or c == cols - 1:
                    ans = max(ans, 1)
                    continue

                matrix[r][c] = (
                    min(matrix[r + 1][c], matrix[r][c + 1], matrix[r + 1][c + 1]) + 1
                )
                ans = max(matrix[r][c], ans, 1)

        return ans**2
