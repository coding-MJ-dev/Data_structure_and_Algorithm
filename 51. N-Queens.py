# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posd = set()
        negd = set()

        ans = []
        grid = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                ans.append([''.join(row) for row in grid])
                return
            
            for c in range(n):
                if c in cols or (r+c) in posd or (r-c) in negd:
                    continue
                grid[r][c] = 'Q'
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)

                dfs(r+1)
                grid[r][c] = '.'
                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
        dfs(0)
        return ans


