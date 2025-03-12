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



    # def countSubstrings(self, s: str) -> int:
    #     ans = 0
    #     for i in range(len(s)):
    #         ans += self.helper(s, i, i)
    #         ans += self.helper(s, i, i+1)
    #     return ans
    
    # def helper(self, s, l, r):
    #     count = 0
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #         count += 1
    #     return count
