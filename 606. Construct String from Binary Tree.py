# 606. Construct String from Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        ans = str(root.val)
        if root.left:
            ans += "(" + self.tree2str(root.left) + ")"
        if root.right and not root.left:
            ans += "()"
        if root.right:
            ans += "(" + self.tree2str(root.right) + ")"

        return ans
