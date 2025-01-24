# 40. Combination Sum II


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort(reverse=True)

        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                ans.append(cur[:])
                return
            if i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                if cur_sum + candidates[j] <= target: 
                    dfs(j+1, cur+[candidates[j]], cur_sum + candidates[j])

        dfs(0, [], 0)
        return ans
        

        # candidates.sort()
        # ans = []

        # def dfs(i, cur, curSum):
        #     nonlocal ans
        #     if curSum == target:
        #         ans.append(cur[:])
        #         return
        #     if i >= len(candidates) or curSum > target:
        #         return

        #     for j in range(i, len(candidates)):
        #         if j > i and candidates[j] == candidates[j - 1]:
        #             continue
        #         dfs(j + 1, cur + [candidates[j]], curSum + candidates[j])

        # dfs(0, [], 0)
        # return ans
