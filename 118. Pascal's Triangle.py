# 118. Pascal's Triangle


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans

        for i in range(1, numRows):
            cur = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(cur)

        return ans
