# 103. Binary Tree Zigzag Level Order Traversal


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        q = deque()
        q.append(root)

        ans = []
        zig = 1

        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zig > 0:
                ans.append(cur)
                zig *= -1
            else:

                ans.append(reversed(cur))
                zig *= -1

        return ans
