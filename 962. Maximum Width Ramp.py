# 962. Maximum Width Ramp


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, n in enumerate(nums):
            if not stack or nums[stack[-1]] >= n:
                stack.append(i)

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ind = stack.pop()
                # print(i, ind)
                ans = max(i - ind, ans)

            if not stack:
                break

        return ans
