class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(i):
            if preMap[i] == []:
                return True
            if i in visit:
                return False

            visit.add(i)
            for nei in preMap[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            preMap[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


sol = Solution()

# 인스턴스를 통해 메서드 호출
v = sol.canFinish(2, [[1, 0]])
print(v)
print(sol.canFinish(2, [[1, 0], [0, 1]]))
