# 759. Employee Free Time


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        work = [x for s in schedule for x in s]
        work.sort(key=lambda x: x.start)
        pre_end = work[0].end
        ans = []
        for w in work[1:]:
            if pre_end >= w.start or w.end <= pre_end:
                pre_end = max(pre_end, w.end)
            else:
                ans.append(Interval(pre_end, w.start))
                pre_end = w.end

        return ans
