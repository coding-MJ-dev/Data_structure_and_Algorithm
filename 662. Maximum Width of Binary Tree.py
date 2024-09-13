# 662. Maximum Width of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))

        ans = 0
        while q:
            cur = []
            for _ in range(len(q)):
                node, n = q.popleft()
                cur.append(n)
                if node.left:
                    q.append((node.left, n * 2))
                if node.right:
                    q.append((node.right, n * 2 + 1))

            ans = max(ans, cur[-1] - cur[0] + 1)
        return ans
