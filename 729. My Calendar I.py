# 729. My Calendar I


class MyCalendar:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        ind = bisect_left(self.cal, [start, end])
        if (ind > 0 and start < self.cal[ind - 1][1]) or (
            ind <= len(self.cal) - 1 and end > self.cal[ind][0]
        ):
            return False
        else:
            bisect.insort(self.cal, [start, end])
            # print(self.cal)
            return True
