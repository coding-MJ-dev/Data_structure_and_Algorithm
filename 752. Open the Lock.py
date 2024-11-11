# 752. Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        ans = []
        visit = set(deadends)

        def change(lock):
            ans = []
            for i in range(4):
                ans.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:])
                ans.append(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:])
            return ans
        
        q = deque([("0000", 0)])
        while q:
            node, step = q.popleft()
            if node == target:
                return step
            
            for nei in change(node):
                if nei in visit:
                    continue
                q.append((nei, step+1))
                visit.add(nei)
        
        return -1