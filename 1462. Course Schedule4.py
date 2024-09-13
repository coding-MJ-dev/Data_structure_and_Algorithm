# 1462. Course Schedule 4


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:

        preMap = defaultdict(list)
        for pre, crs in prerequisites:
            preMap[pre].append(crs)

        ansMap = defaultdict(list)

        def dfs(i):
            if i not in ansMap:
                ansMap[i] = set()
                for crs in preMap[i]:
                    ansMap[i] |= dfs(crs)
            ansMap[i].add(i)
            return ansMap[i]

        for i in range(numCourses):
            dfs(i)

        ans = []
        for pre, crs in queries:
            if crs in ansMap[pre]:
                ans.append(True)
            else:
                ans.append(False)

        return ans
