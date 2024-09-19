# 128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        check = sorted(list(set(nums)))
        if len(check) <= 1:
            return len(check)

        ans = 1
        count = 1
        for i in range(1, len(check)):
            if check[i] - check[i - 1] == 1:
                # print(check[i])
                count += 1
                ans = max(count, ans)
            else:
                count = 1
        return ans
