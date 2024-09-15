# 77. Combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(i, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return
            if i >= n + 1 or len(cur) > k:
                return

            dfs(i + 1, cur + [i])
            dfs(i + 1, cur)

        dfs(1, [])
        return ans
