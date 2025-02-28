# 90. Subsets II


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(i, cur):
            if i >= len(nums):
                ans.append(cur[:])
                return

            dfs(i + 1, cur + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, cur)

        dfs(0, [])
        return ans
