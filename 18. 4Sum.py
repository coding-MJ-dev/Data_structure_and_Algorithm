# 18. 4Sum


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # if nums[a] > target:
            #     break
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                # if nums[a] + nums[b] > target:
                #     break
                c, d = b + 1, len(nums) - 1
                while c < d:
                    curSum = nums[a] + nums[b] + nums[c] + nums[d]
                    if curSum == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                    elif curSum > target:
                        d -= 1
                    else:
                        c += 1

        return ans
