# 40. Combination Sum II


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, cur, curSum):
            nonlocal ans
            if curSum == target:
                ans.append(cur[:])
                return
            if i >= len(candidates) or curSum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                dfs(j + 1, cur + [candidates[j]], curSum + candidates[j])

        dfs(0, [], 0)
        return ans
