# 473. Matchsticks to Square
class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        if sum(ms) % 4 > 0:
            return False
        target = sum(ms) //4

        ms.sort(reverse=True)
        if ms[0] > target:
            return False
        
        side = [0] * 4

        def dfs(i):
            if i == len(ms):
                return True
            
            for j in range(4):
                if side[j] + ms[i] <= target:
                    side[j] += ms[i]
                    if dfs(i+1):
                        return True
                    side[j] -= ms[i]
                    if side[j] == 0:
                        return False
            return False
        
        return dfs(0)


