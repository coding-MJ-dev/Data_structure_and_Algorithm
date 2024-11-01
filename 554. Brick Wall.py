# 554. Brick Wall


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = defaultdict(int)
        wall_len = sum(wall[0])

        for w in wall:
            prefix = 0
            for b in w:
                prefix += b
                if prefix != wall_len:
                    dic[prefix] += 1
        # print(dic, wall_len)
        return len(wall) - max(dic.values()) if dic else len(wall)
