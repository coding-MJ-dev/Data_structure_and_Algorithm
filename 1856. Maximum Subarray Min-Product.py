# 1856. Maximum Subarray Min-Product

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        stack = [] # [cover index, val]
        prefix = [0] 
        for n in nums:
            prefix.append(prefix[-1] + n)

        nums.append(0)
        ans = 0
        for i, n in enumerate(nums):
            starting = i
            while stack and stack[-1][1] > n:
                popInd, val = stack.pop()
                curSum = prefix[i] - prefix[popInd]
                # print(curSum, val, popInd)
                ans = max(curSum * val , ans)
                starting = popInd
            stack.append((starting, n))
        # print(stack)
        return ans % mod
