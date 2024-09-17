# 80. Remove Duplicates from Sorted Array II


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 2
        for j in range(2, len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i
