# 2140. Solving Questions With Brainpower

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            score, skip = questions[i][0], questions[i][1] + 1
            dp[i] = max(dp[i+1], score + (dp[i+skip] if i+skip < len(questions) else 0))

        return dp[0]