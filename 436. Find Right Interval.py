# 436. Find Right Interval

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = {val[0]: i for i, val in enumerate(intervals)}
        vals = [val[0] for val in intervals]
        vals.sort()

        ans = []
        for s, e in intervals:
            ind = bisect.bisect_left(vals, e)
            if ind == len(intervals):
                ans.append(-1)
            elif e in start:
                ans.append(start[e])
            else:
                ans.append(start[vals[ind]])
 
        return ans

    
    # gpt solution
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#             # Create a sorted list of start times with their original indices
#         starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
#         result = []
        
#         for interval in intervals:
#             # Use binary search to find the smallest start >= current end
#             target = interval[1]
#             left, right = 0, len(starts)
#             while left < right:
#                 mid = (left + right) // 2
#                 if starts[mid][0] >= target:
#                     right = mid
#                 else:
#                     left = mid + 1

#             # Append the result index or -1 if no valid interval is found
#             result.append(starts[left][1] if left < len(starts) else -1)
        
#         return result
