# 295. Find Median from Data Stream

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:
    def __init__(self):
        self.lefthp = []  # -v to find the largest number
        self.righthp = []  # v for find the smallest number
        heapify(self.lefthp)
        heapify(self.righthp)

    def addNum(self, num: int) -> None:
        if len(self.righthp) == len(self.lefthp):
            heappush(self.righthp, -heappushpop(self.lefthp, -num))
        else:
            heappush(self.lefthp, -heappushpop(self.righthp, num))

    def findMedian(self) -> float:
        if (len(self.righthp) + len(self.lefthp)) % 2:
            return self.righthp[0] * 1.0
        else:
            return (self.righthp[0] - self.lefthp[0]) / 2
