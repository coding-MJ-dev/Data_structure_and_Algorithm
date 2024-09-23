# 210. Course Schedule2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        preNum = [0] * numCourses

        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            preNum[crs] += 1

        q = deque()
        for i in range(numCourses):
            if preNum[i] == 0:
                q.append(i)

        ans = []
        while q:
            pre = q.popleft()
            ans.append(pre)
            for crs in preMap[pre]:
                preNum[crs] -= 1
                if preNum[crs] == 0:
                    q.append(crs)

        return ans if len(ans) == numCourses else []
