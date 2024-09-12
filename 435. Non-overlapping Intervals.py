# 435. Non-overlapping Intervals


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        stack = []
        count = 0
        for start, end in intervals:
            if stack and stack[-1][1] > start:
                stack[-1][1] = min(stack[-1][1], end)
                count += 1
            else:
                stack.append([start, end])

        return count
