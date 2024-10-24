# 22. Generate Parentheses


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(l, r, cur):
            if l == n and r == n:
                ans.append("".join(cur[:]))
                return

            if l < n:
                dfs(l + 1, r, cur + ["("])

            if r < l:
                dfs(l, r + 1, cur + [")"])

        dfs(0, 0, [])
        return ans
