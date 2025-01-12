# 1926. Nearest Exit from Entrance in Maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        exit = set()
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows -1) and maze[i][j] == ".":
                    exit.add((i, j))
                if (j == 0 or j == cols -1) and maze[i][j] == ".":
                    exit.add((i, j))
        enter = tuple(entrance)
        exit.discard(enter)

        visit = set([enter])
        q = deque()
        q.append((enter, 0))

        while q:
            (i, j), dist = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = i + dr, j + dc
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == "." and (r, c) not in visit:
                    if (r, c) in exit:
                        return dist + 1
                    visit.add((r, c))
                    q.append(((r,c), dist+1))
        
        return -1