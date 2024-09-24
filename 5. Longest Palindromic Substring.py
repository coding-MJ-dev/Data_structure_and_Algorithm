# 5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        I, J = 0, 0

        def isP(i, j):
            nonlocal ans, I, J
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                if j - i + 1 > ans:
                    ans = max(ans, j - i + 1)
                    I = i
                    J = j
                i -= 1
                j += 1

        for i in range(len(s)):
            isP(i, i)
            isP(i, i + 1)

        return s[I : J + 1]
