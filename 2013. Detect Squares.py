# 2013. Detect Squares

class DetectSquares:

    def __init__(self):
        self.side = defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.side[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0

        for s in self.side:
            x2, y2 = s
            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:
                side1 = self.side[(x1, y2)] if (x1, y2) in self.side else 0
                side2 = self.side[(x2, y1)] if (x2, y1) in self.side else 0
                ans += self.side[(x2, y2)] * side1 * side2
        return ans
