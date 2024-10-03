# 47. Permutations II


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(cur, nums):
            if not nums:
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(cur + [nums[i]], nums[:i] + nums[i + 1 :])

        dfs([], nums)
        return ans
