# 909. Snakes and Ladders


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        end = rows * cols
        board.reverse()

        def intToPos(n):
            n = n - 1
            r = n // rows
            c = n % rows
            if r % 2 == 0:
                return (r, c)
            else:
                return (r, cols - c - 1)

        visit = set()
        q = deque()
        q.append((1, 0))  # pos, step
        visit.add(1)

        while q:
            pos, step = q.popleft()
            # if pos == end:
            #     return step

            for i in range(1, 7):
                if pos + i in visit:
                    continue
                visit.add(pos + i)
                r, c = intToPos(pos + i)
                # print(pos+i, r, c, step)
                # print(q)
                if board[r][c] == -1:
                    if pos + i == end:
                        return step + 1
                    q.append((pos + i, step + 1))
                else:
                    # print(1)
                    if board[r][c] == end:
                        return step + 1
                    q.append((board[r][c], step + 1))

        return -1
