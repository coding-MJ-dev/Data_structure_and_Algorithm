# 841. Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set([0])
        n = len(rooms)
        q = deque([0])
        while q:
            room = q.popleft()
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    visit.add(key)
                    q.append(key)
        
        return len(visit) == n
