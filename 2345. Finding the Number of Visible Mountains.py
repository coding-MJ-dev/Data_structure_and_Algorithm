# 2345. Finding the Number of Visible Mountains
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        left_seen = [-float('inf')]
        last_seen = -float('inf')
        peaks.sort()
        for x, y in peaks:
            left = x - y
            right= x + y
            while left_seen[-1] >= left:
                left_seen.pop()
            if right > last_seen:
                left_seen.append(left)
                last_seen = right

        return len(left_seen) - 1
