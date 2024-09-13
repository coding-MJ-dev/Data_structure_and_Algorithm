# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder and postorder:
            val = postorder.pop()
            ind = inorder.index(val)
            root = TreeNode(val)

            root.right = self.buildTree(inorder[ind + 1 :], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
