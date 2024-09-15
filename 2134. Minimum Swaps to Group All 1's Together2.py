# 2134. Minimum Swaps to Group All 1's Together2
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if sum(nums) <= 1:
            return 0
        counts = nums.count(1)
        nums[:] = nums[:] + nums[:]
        ones = sum(nums[:counts])
        maxOnes = ones

        i = 0
        for j, n in enumerate(nums[counts:]):
            ones = ones - nums[i] + n
            maxOnes = max(ones, maxOnes)
            i += 1

        return counts - maxOnes
