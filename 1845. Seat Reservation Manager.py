# 1845. Seat Reservation Manager


class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]
        self.dic = {i: True for i in range(1, n + 1)}

    def reserve(self) -> int:
        seat = heappop(self.heap)
        self.dic[seat] = False
        return seat

    def unreserve(self, seatNumber: int) -> None:
        if self.dic[seatNumber] == False:
            self.dic[seatNumber] = True
            heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
