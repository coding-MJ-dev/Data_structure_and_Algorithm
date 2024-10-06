# 286. Walls and Gates


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 1
        while q:
            # print(rooms)
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    i, j = r + dr, c + dc
                    if (
                        0 <= i < rows
                        and 0 <= j < cols
                        and (i, j) not in visit
                        and rooms[i][j] != -1
                    ):
                        rooms[i][j] = dist
                        visit.add((i, j))
                        q.append((i, j))
            dist += 1
