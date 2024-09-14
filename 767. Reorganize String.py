# 767. Reorganize String


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        hp = [(-v, k) for k, v in count.items()]
        heapify(hp)

        ans = ""
        pre_v, pre_k = None, None
        while hp:
            v, k = heappop(hp)
            ans += k
            if pre_v and pre_v < 0:
                heappush(hp, (pre_v, pre_k))
            pre_v, pre_k = v + 1, k

        return ans if len(ans) == len(s) else ""
