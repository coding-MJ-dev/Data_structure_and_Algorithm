# 215. Kth Largest Element in an Array


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for n in nums:
            heappush(hp, n)
            if len(hp) > k:
                heappop(hp)
        return heappop(hp)
