# 1911. Maximum Alternating Subsequence Sum


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd, even = 0, 0
        for i in range(len(nums)-1, -1, -1):
            curOdd = max(even + nums[i], odd)
            curEven = max(odd - nums[i], even)
            odd, even = curOdd, curEven
        
        return odd