# 846. Hand of Straights
# oh no


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = collections.Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        number = len(hand) // groupSize
        heapify(hand)
        # print(hand)
        # print(count)
        for _ in range(number):

            val = heappop(hand)
            while count[val] == 0:
                val = heappop(hand)
            count[val] -= 1
            # print(count)
            c = 1
            # print(val)
            while c < groupSize:
                if val + 1 in count and count[val + 1] > 0:
                    c += 1
                    count[val + 1] -= 1
                    val += 1
                else:
                    return False

        return True
