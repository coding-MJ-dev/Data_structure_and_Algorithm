# 1834. Single-Threaded CPU


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        heap = []
        tasks.sort()
        q = deque(tasks)
        ans = []
        time = q[0][0]
        while q or heap:
            while q and q[0][0] <= time:
                _, process, i = q.popleft()
                heapq.heappush(heap, (process, i))
            if heap:
                t, i = heappop(heap)
                time += t
                ans.append(i)
            else:
                time = q[0][0]

        return ans
