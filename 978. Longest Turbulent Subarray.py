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



        # compare = 0
        # ans = 1
        # cur = 1
        # for i in range(1, len(arr)):
        #     if (arr[i] - arr[i-1] < 0 and compare >= 0) or (arr[i] - arr[i-1] > 0 and compare <= 0):
        #         # print(arr[i])
        #         compare = arr[i] - arr[i-1]
        #         cur += 1
        #         ans = max(ans, cur)
        #     else:
        #         # cur = 1
        #         # compare = 0
        #         cur = 2 if arr[i] != arr[i-1] else 1
        #         compare = arr[i] - arr[i-1]
        # return ans