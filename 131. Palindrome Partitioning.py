# 131. Palindrome Partitioning


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPal(i, j):
            check = s[i : j + 1]
            return check == check[::-1]

        def dfs(i, cur):
            if i == len(s):
                ans.append(cur[:])
                return

            for j in range(i, len(s)):
                if isPal(i, j):
                    dfs(j + 1, cur + [s[i : j + 1]])

        dfs(0, [])
        return ans
