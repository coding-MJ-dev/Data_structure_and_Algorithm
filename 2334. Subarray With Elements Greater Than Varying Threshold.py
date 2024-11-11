# 2334. Subarray With Elements Greater Than Varying Threshold

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = [-1] # inc
        nums.append(0)
        for i, n in enumerate(nums):
            while nums[stack[-1]] > n:
                popInd = stack.pop()
                val = nums[popInd]
                length = i - stack[-1] - 1
                if val > threshold / length:
                    return length
            stack.append(i)
        return -1

