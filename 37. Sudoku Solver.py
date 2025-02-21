# 37. Sudoku Solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        x = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    n = board[i][j]
                    rows[i].add(n)
                    cols[j].add(n)
                    boxs[(i//3)*3 + (j//3)].add(n)
                else:
                    x.append((i, j))
        
        def check(i, j, n):
            if n in rows[i] or n in cols[j] or n in boxs[(i//3)*3 + (j//3)]:
                return False
            return True
        
        def solve(ind):
            if ind == len(x):
                return True

            i, j = x[ind]
            boxInd = (i//3)*3 + (j//3)
            for n in "123456789":
                if check(i, j, n):
                    board[i][j] = n
                    rows[i].add(n)
                    cols[j].add(n)
                    boxs[boxInd].add(n)

                    if solve(ind + 1):
                        return True
                    
                    board[i][j] = "."
                    rows[i].remove(n)
                    cols[j].remove(n)
                    boxs[boxInd].remove(n)
        
        solve(0)