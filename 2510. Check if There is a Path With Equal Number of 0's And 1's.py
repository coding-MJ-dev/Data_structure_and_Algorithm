# 2510. Check if There is a Path With Equal Number of 0's And 1's

# from functools import lru_cache


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        zeros, ones = 0, 0
        rows, cols = len(grid), len(grid[0])
        if (rows + cols - 1) % 2 == 1:
            return False
        limits = (rows + cols - 1) // 2

        dic = {}

        # @lru_cache
        def dfs(r, c, z, o):
            nonlocal dic
            if r < 0 or r >= rows or c < 0 or c >= cols:
                dic[(r, c, z, o)] = False
                return dic[(r, c, z, o)]

            if grid[r][c] == 1:
                o += 1
            else:
                z += 1

            if r == rows - 1 and c == cols - 1 and z == o:
                dic[(r, c, z, o)] = True
                return dic[(r, c, z, o)]

            if z > limits or o > limits:
                dic[(r, c, z, o)] = False
                return dic[(r, c, z, o)]

            if (r, c, z, o) in dic:
                return dic[(r, c, z, o)]

            dic[(r, c, z, o)] = dfs(r + 1, c, z, o) or dfs(r, c + 1, z, o)
            return dic[(r, c, z, o)]

        return dfs(0, 0, zeros, ones)
