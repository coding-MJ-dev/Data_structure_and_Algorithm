# 46. Permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(arr, cur):
            if not arr:
                ans.append(cur[:])
                return

            for i in range(len(arr)):
                cur.append(arr[i])
                dfs(arr[:i] + arr[i + 1 :], cur)
                cur.pop()

        dfs(nums, [])
        return ans
