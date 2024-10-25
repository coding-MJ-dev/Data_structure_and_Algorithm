# 981. Time Based Key-Value Store


class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        lst = self.map[key]
        l, r = 0, len(lst) - 1

        while l <= r:
            m = l + (r - l) // 2
            time = lst[m][0]
            if time <= timestamp:
                ans = lst[m][1]
                l = m + 1
            else:
                r = m - 1

        return ans
