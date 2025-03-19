# 198. House Robber


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = rob1 + n
            rob1 = rob2
            rob2 = max(temp, rob2)
        return rob2