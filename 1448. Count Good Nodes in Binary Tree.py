# 1448. Count Good Nodes in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        val = root.val
        ans = 0

        def dfs(node, val):
            nonlocal ans
            if not node:
                return 0
            if node.val >= val:
                ans += 1

            val = max(node.val, val)
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, val)
        return ans
