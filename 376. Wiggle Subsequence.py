# 376. Wiggle Subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # O(n), O(1)
        if not nums:
            return 0
            
        last = 0
        ans = 1

        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1] > 0 and last <= 0) or (nums[i] - nums[i-1] < 0 and last >= 0):
                ans += 1
                last = nums[i] - nums[i-1]
        
        return ans







        # # O(n2), O(n)
        # ans = 1
        # dp = {(len(nums)-1, True): 1, (len(nums)-1, False): 1} # key: ind, True(+)/False(-) / val: length )
        
        # for i in range(len(nums)-2, -1, -1):

        #     dp[(i, True)] = 1
        #     dp[(i, False)] = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             dp[(i, True)] = max(dp[(i, True)], dp[(j, False)] + 1)
        #         elif nums[i] < nums[j]:
        #             dp[(i, False)] = max(dp[(i, False)] , dp[(j, True)] + 1)

        # return max(dp[(0,True)], dp[(0,False)])