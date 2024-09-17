# 26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        seen = set()
        for j in range(len(nums)):
            if nums[j] not in seen:
                nums[i] = nums[j]
                i += 1
                seen.add(nums[j])

        return i
