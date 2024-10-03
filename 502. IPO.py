# 502. IPO


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        hp = [(x, y) for x, y in zip(capital, profits)]
        heapify(hp)

        ans = w
        work = []
        while k > 0:
            while hp and hp[0][0] <= ans:
                cap, pro = heappop(hp)
                heappush(work, -pro)
            # print(hp, work)
            if work:
                ans += -heappop(work)
            k -= 1

        return ans
