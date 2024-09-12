# 124. Binary Tree Maximum Path Sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = root.val

        def dfs(node, curSum):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left, curSum)
            right = dfs(node.right, curSum)
            res = max(res, node.val + max(left, 0) + max(right, 0))

            return node.val + max(left, right, 0)

        dfs(root, 0)
        return res
