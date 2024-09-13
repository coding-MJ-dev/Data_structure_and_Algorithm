# 79. Word Search


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i]:
                if i == len(word) - 1:
                    return True
                board[r][c] = "*"
                res = (
                    dfs(i + 1, r + 1, c)
                    or dfs(i + 1, r, c + 1)
                    or dfs(i + 1, r - 1, c)
                    or dfs(i + 1, r, c - 1)
                )
                board[r][c] = word[i]
                return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        return False
