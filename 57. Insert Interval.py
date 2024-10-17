# 57. Insert Interval


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        stack = [intervals[0]]
        for start, end in intervals:
            if start > stack[-1][1]:
                stack.append([start, end])
            else:
                old_start, old_end = stack.pop()
                stack.append([min(old_start, start), max(old_end, end)])

        return stack
