# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()  # min num
        dec = deque()  # max num in arr

        i = 0
        j = 0
        ans = 0
        while j < len(nums):
            while inc and nums[inc[-1]] > nums[j]:
                inc.pop()
            while dec and nums[dec[-1]] < nums[j]:
                dec.pop()
            inc.append(j)
            dec.append(j)
            while nums[dec[0]] - nums[inc[0]] > limit:
                if dec[0] == i:
                    dec.popleft()
                if inc[0] == i:
                    inc.popleft()
                i += 1
            ans = max(ans, j - i + 1)
            j += 1

        return ans
