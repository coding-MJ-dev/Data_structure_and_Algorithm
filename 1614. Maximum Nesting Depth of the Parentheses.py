# 1614. Maximum Nesting Depth of the Parentheses


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
                ans = max(len(stack), ans)
            elif c == ")":
                stack.pop()

        return ans
