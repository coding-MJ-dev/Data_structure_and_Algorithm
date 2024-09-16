# 39. Combination Sum


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, cur, curSum):
            if curSum == target:
                ans.append(cur[:])
                return
            if i >= len(candidates) or curSum > target:
                return
            dfs(i, cur + [candidates[i]], curSum + candidates[i])
            dfs(i + 1, cur, curSum)

        dfs(0, [], 0)
        return ans
