# 303. Range Sum Query - Immutable


class NumArray:

    def __init__(self, nums: List[int]):
        self.sumDic = {-1: 0}
        curSum = 0
        for i, n in enumerate(nums):
            curSum += n
            self.sumDic[i] = curSum

    def sumRange(self, left: int, right: int) -> int:
        return self.sumDic[right] - self.sumDic[left - 1]
