# 1361. Validate Binary Tree Nodes

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # no cycle, all nodes should be connected, 1 root

        child = set(leftChild + rightChild)
        child.discard(-1)
        if len(child) != n-1:
            return False
        
        root = -1
        for i in range(n):
            if i not in child:
                root = i
                break
        
        #find cycle
        visit = set()
        def dfs(node):
            if node == -1:
                return True
            if node in visit:
                return False

            visit.add(node)

            if leftChild[node] == -1 and rightChild[node] == -1:
                return True

            return dfs(leftChild[node]) and dfs(rightChild[node])
            
        
        return dfs(root) and len(visit) == n