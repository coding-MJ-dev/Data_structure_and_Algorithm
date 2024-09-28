# 621. Task Scheduler


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        q = deque()
        hp = [v * -1 for v in dic.values()]
        heapify(hp)
        time = 0

        while hp or q:
            if hp:
                work = heappop(hp)
                work += 1
                if work < 0:
                    q.append((time + n, work))

            if q and q[0][0] == time:
                _, pre_work = q.popleft()
                heappush(hp, pre_work)
            time += 1

        return time
