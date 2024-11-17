# 1029. Two City Scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        hq = [(x-y, x, y) for x, y in costs]
        hq.sort()
        # print(hq)
        ans += sum([x[1] for x in hq[:len(costs)//2]])
        ans += sum([x[2] for x in hq[len(costs)//2:]])
        
        return ans



# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         costs.sort(key=lambda x: x[0] - x[1])
#         n = len(costs) // 2
#         return sum(costs[i][0] for i in range(n)) + sum(costs[i][1] for i in range(n, 2*n))