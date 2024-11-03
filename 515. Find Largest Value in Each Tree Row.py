# 515. Find Largest Value in Each Tree Row


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])

        while q:
            cur = -float("inf")
            for _ in range(len(q)):
                node = q.popleft()
                cur = max(node.val, cur)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(cur)
        return ans
