# 2502. Design Memory Allocator


class Allocator:

    def __init__(self, n: int):
        self.m = [-1] * n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i, n in enumerate(self.m):
            if n == -1:
                count += 1
            else:
                count = 0
            if count == size:
                self.m[i - size + 1 : i + 1] = [mID] * size
                return i - size + 1
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i, n in enumerate(self.m):
            if n == mID:
                count += 1
                self.m[i] = -1

        return count
