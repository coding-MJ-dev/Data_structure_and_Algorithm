# 3043. Find the Length of the Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()

        for n in arr2:
            while n > 0:
                prefix.add(n)
                n //= 10
        ans = 0
        for n in arr1:
            while n > ans:
                if n in prefix:
                    ans = max(n, ans)
                n //= 10

        return len(str(ans)) if ans > 0 else 0
