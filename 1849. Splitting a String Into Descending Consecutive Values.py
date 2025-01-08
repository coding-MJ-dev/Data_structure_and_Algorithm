# 1849. Splitting a String Into Descending Consecutive Values

class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i, prev):
            if i == len(s):
                return True

            for j in range(i+1, len(s)+1):
                cur = int(s[i:j])
                if cur == prev-1:
                    if dfs(j, cur):
                        return True
            return False

        for i in range(1, len(s)):
            if dfs(i, int(s[:i])):
                return True
        return False