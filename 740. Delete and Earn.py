# 740. Delete and Earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums = list(set(nums))
        earn1, earn2 = 0, 0
        for i, n in enumerate(nums):
            val = n * count[n]
            if i > 0  and nums[i] - nums[i-1] == 1:
                temp = max(earn1+val, earn2)
                earn1 = earn2
                earn2 = temp
            else:
                temp = earn2 + val
                earn1 = earn2
                earn2 = temp
            
        return earn2