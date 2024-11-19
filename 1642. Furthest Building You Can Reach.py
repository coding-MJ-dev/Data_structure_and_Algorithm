# 1642. Furthest Building You Can Reach

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = [] # max heap

        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            if gap <= 0:
                continue
            bricks -= gap
            heappush(hp, -gap)

            if bricks < 0:
                if not ladders:
                    return i
                else:
                    ladders -= 1
                    if hp:
                        bricks -= heappop(hp)
            
        return len(heights) - 1
