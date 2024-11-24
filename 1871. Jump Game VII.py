# 1871. Jump Game VII

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] == "1" or s[-1] == "1":
            return False
        q = deque([0])
        visit = 0

        while q:
            i = q.popleft()
            if i == len(s) -1:
                return True
            if s[i] == "1":
                continue
            next_check = max(i + minJump, visit+1)
            for j in range(next_check, min(i + maxJump + 1, len(s))):
                if j == len(s) -1:
                    return True
                q.append(j)
                visit = max(j, next_check)