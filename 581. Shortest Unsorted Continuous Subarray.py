# 581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        min_i = len(nums)
        max_i = -1

        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                min_i = min(min_i, i)
                max_i = max(max_i, i)

        return max_i - min_i + 1 if min_i != len(nums) else 0
