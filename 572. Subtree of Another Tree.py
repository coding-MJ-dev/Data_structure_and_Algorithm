# 572. Subtree of Another Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # at this point we;re sure both tree exists in the very beginning
        def find(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False

            return find(l.left, r.left) and find(l.right, r.right)

        return (
            find(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
