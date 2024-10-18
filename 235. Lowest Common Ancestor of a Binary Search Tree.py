# 235. Lowest Common Ancestor of a Binary Search Tree


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return

        if root.val == p.val:
            return p

        if root.val == q.val:
            return q

        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
