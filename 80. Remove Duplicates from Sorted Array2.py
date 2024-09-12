class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 2
        for j in range(2, len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i


sol = Solution()

print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
