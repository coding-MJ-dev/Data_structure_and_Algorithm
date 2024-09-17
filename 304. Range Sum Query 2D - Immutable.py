# 304. Range Sum Query 2D - Immutable


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dp = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for i in range(self.rows):
            curSum = 0
            for j in range(self.cols):
                curSum += matrix[i][j]
                # print(curSum)
                self.dp[i + 1][j + 1] = curSum + self.dp[i][j + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )
