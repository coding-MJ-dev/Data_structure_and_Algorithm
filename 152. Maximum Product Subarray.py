# 152. Maximum Product Subarray


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum = nums[0]
        maxNum = nums[0]
        res = nums[0]

        for n in nums[1:]:

            minNum, maxNum = min(minNum * n, maxNum * n, n), max(
                minNum * n, maxNum * n, n
            )

            res = max(minNum, maxNum, res)

        return res
