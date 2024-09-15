# 1466. Reorder Routes to Make All Paths Lead to the City Zero


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roadMap = defaultdict(list)
        dirMap = defaultdict(list)

        for start, end in connections:
            dirMap[start].append(end)
            roadMap[start].append(end)
            roadMap[end].append(start)
        q = deque()
        q.append((0, None))  # node, prev
        count = 0

        while q:
            node, prev = q.popleft()
            if node != 0 and prev not in dirMap[node]:
                count += 1
                dirMap[node].append(0)
            for nei in roadMap[node]:
                if nei == prev:
                    continue
                q.append((nei, node))

        return count
