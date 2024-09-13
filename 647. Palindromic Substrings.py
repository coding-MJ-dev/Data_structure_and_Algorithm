# 647. Palindromic Substrings


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPal(i, j):
            nonlocal count
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

        for i in range(len(s)):
            isPal(i, i)
            isPal(i, i + 1)
        return count
