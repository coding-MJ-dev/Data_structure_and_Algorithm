# 2104. Sum of Subarray Ranges 

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        small_sum = 0
        large_sum = 0
        
        stack = [-1]
        nums.append(-float('inf'))
        for i, n in enumerate(nums):
            while nums[stack[-1]] > n:
                popInd = stack.pop()
                val = nums[popInd]
                small_sum += (popInd - stack[-1]) * (i - popInd) * val
            stack.append(i)

        stack = [-1]
        nums[-1] = float('inf')
        for i, n in enumerate(nums):
            while nums[stack[-1]] < n:
                popInd = stack.pop()
                val = nums[popInd]
                large_sum += (popInd - stack[-1]) * (i - popInd) * val
            stack.append(i)
        
        return large_sum - small_sum