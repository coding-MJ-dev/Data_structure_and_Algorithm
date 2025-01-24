# 238. Product of Array Except Self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        
        return ans







        # check = nums.count(0)
        # if check >= 2:
        #     return [0] * len(nums)

        # mul = 1
        # for n in nums:
        #     if n != 0:
        #         mul *= n

        # ans = []
        # for n in nums:
        #     if check == 0:
        #         ans.append(mul // n)
        #     elif check == 1:
        #         if n != 0:
        #             ans.append(0)
        #         else:
        #             ans.append(mul)
        # return ans
