# 978. Longest Turbulent Subarray


class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        incresing, decresing = 1, 1
        ans = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decresing = incresing + 1
                incresing = 1
            elif nums[i] < nums[i+1]:
                incresing = decresing + 1
                decresing = 1
            else:
                incresing, decresing = 1, 1
            ans = max(ans, incresing, decresing)
        
        return ans
