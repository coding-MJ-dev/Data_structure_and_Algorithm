# 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = 1
        ans = [""] * numRows
        curRow = 0
        for c in s:
            if curRow == 0:
                step = 1

            elif curRow == numRows - 1:
                step = -1

            ans[curRow] += c
            curRow += step
        return "".join(ans)
