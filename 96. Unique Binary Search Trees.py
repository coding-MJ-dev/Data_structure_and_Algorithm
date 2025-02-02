# 96. Unique Binary Search Trees


class Solution:
    def numTrees(self, n: int) -> int:
        dic = {0:1, 1: 1}

        def dfs(num):
            if num in dic:
                return dic[num]
            
            val = 0
            for root in range(1, num + 1):
                left = root - 1
                right = num - root
                val += dfs(left) * dfs(right)
            
            dic[num] = val
            return val
        
        return dfs(n)