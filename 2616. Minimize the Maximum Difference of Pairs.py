# 2616. Minimize the Maximum Difference of Pairs

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]

        def check(m):
            count = 0
            i = 0
            while i < len(nums) -1:
                if nums[i+1] - nums[i] <= m:
                    count+=1
                    i += 2
                else:
                    i += 1
            return True if count >= p else False
                 
        ans = r
        while l <= r:
            m = l + (r - l) // 2

            if check(m):
                ans = min(m, ans)
                r = m - 1
            else:
                l = m + 1
        return ans