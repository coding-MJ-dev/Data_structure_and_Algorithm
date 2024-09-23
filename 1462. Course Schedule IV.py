# 1462. Course Schedule IV


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        preMap = defaultdict(list)
        for pre, crs in prerequisites:
            preMap[crs].append(pre)

        ansMap = defaultdict(list)

        def dfs(i):
            if i not in ansMap:
                ansMap[i] = set()
                for pre in preMap[i]:
                    ansMap[i] |= dfs(pre)
                ansMap[i].add(i)
            return ansMap[i]

        for i in range(numCourses):
            dfs(i)

        ans = []
        for q1, q2 in queries:
            if q1 in ansMap[q2]:
                ans.append(True)
            else:
                ans.append(False)

        return ans
