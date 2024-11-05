class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
                








        # dp = {}
        
        # def dfs(r, c):
        #     if r == len(triangle)-1:
        #         return triangle[len(triangle)-1][c]
            
        #     if (r, c) in dp:
        #         return dp[(r, c)]

        #     left = dfs(r+1, c)
        #     right = dfs(r+1, c+1)
        #     ans = triangle[r][c] + min(left, right)

        #     dp[(r, c)] = ans
        #     return ans
   
        # return dfs(0, 0)





        # dp = [0] * (len(triangle) + 1)

        # for row in triangle[::-1]:
        #     for i, n in enumerate(row):
        #         dp[i] = n + min(dp[i], dp[i+1])
        
        # return dp[0]