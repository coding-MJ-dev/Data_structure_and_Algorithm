# 149. Max Points on a Line


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points) - 1):
            p1 = points[i]
            lines = defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                lines[slope] += 1
                ans = max(ans, lines[slope] + 1)

        # print(lines)
        return ans
