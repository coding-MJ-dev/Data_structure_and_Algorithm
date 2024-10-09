# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = len(nums) - 1
        while i >= 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0:
            nums[:] = nums[::-1]
            return
        
        i -= 1
        j = len(nums) - 1
 
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
        l = i + 1
        r = len(nums) - 1
        while l <= r :
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
