# 2104. Sum of Subarray Ranges 

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0
        stack = []

        #
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        
        #
        stack.clear()
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid-left) * (right-mid)
            stack.append(right)

        return answer


        # small_sum = 0
        # large_sum = 0
        
        # stack = [-1]
        # nums.append(-float('inf'))
        # for i, n in enumerate(nums):
        #     while nums[stack[-1]] > n:
        #         popInd = stack.pop()
        #         val = nums[popInd]
        #         small_sum += (popInd - stack[-1]) * (i - popInd) * val
        #     stack.append(i)

        # stack = [-1]
        # nums[-1] = float('inf')
        # for i, n in enumerate(nums):
        #     while nums[stack[-1]] < n:
        #         popInd = stack.pop()
        #         val = nums[popInd]
        #         large_sum += (popInd - stack[-1]) * (i - popInd) * val
        #     stack.append(i)
        
        # return large_sum - small_sum