# 1882. Process Tasks Using Servers


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        serverHeap = [(w, i) for i, w in enumerate(servers)]
        heapify(serverHeap)
        taskq = deque([(i, t) for i, t in enumerate(tasks)])
        possibleTaskq = deque()
        processheap = []

        ans = [-1] * len(tasks)
        time = 0
        while taskq or processheap or possibleTaskq:
            # print(taskq, processheap, possibleTaskq, serverHeap)
            while processheap and processheap[0][0] == time:
                finishedTime, ansI, weigh, serverI = heappop(processheap)
                ans[ansI] = serverI
                heappush(serverHeap, (weigh, serverI))

            if taskq and taskq[0][0] == time:
                i, t = taskq.popleft()
                possibleTaskq.append((t, i))

            while serverHeap and possibleTaskq:
                weigh, serverI = heappop(serverHeap)
                t, ansI = possibleTaskq.popleft()
                heappush(processheap, (time + t, ansI, weigh, serverI))
            # time += 1
            time = (
                taskq[0][0] if taskq else processheap[0][0] if processheap else time + 1
            )
            # time = min(processheap[0][0], taskq[0][0] if taskq else inf)

        return ans
