# 114. Flatten Binary Tree to Linked List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        cur = root
        if cur.left:
            walker = runner = cur.left
            while runner.right:
                runner = runner.right

            cur.right, cur.left, runner.right = walker, None, cur.right

        self.flatten(root.right)
