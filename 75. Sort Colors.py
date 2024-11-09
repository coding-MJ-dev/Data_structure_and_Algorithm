# 75. Sort Colors


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        m = 0
        while m <= j:
            if nums[m] == 0:
                nums[i], nums[m] = nums[m], nums[i]
                i += 1
                m += 1
            elif nums[m] == 2:
                nums[m], nums[j] = nums[j], nums[m]
                j -= 1
            else:
                m += 1