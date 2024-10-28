# 74. Search a 2D Matrix


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                print(matrix[m])
                return target in matrix[m]

        return False
