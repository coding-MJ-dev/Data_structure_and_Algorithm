# 253. Meeting Rooms II

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for start, end in intervals:
            if heap and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)
        
        return len(heap)