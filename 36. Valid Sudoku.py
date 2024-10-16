# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]

        # print(square)
        def check(r, c, n):
            if n in row[r]:
                return False
            if n in col[c]:
                return False
            if n in square[r // 3][c // 3]:
                return False
            return True

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":

                    if check(r, c, board[r][c]):
                        row[r].add(board[r][c])
                        col[c].add(board[r][c])
                        square[r // 3][c // 3].add(board[r][c])
                        # print(board[r][c], r, c, r//3, c//3, square)
                    else:
                        # print(r, c, board[r][c], row, col, square)
                        return False

        return True
