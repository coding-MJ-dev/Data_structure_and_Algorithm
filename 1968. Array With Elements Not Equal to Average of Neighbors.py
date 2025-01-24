# 1968. Array With Elements Not Equal to Average of Neighbors

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1
        while l <= r:
            ans.append(nums[l])
            l += 1
            if l < r:
                ans.append(nums[r])
                r -= 1
        return ans