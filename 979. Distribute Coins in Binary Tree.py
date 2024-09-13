# 979. Distribute Coins in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            need_coin = (root.val - 1) + (right + left)
            ans += abs(need_coin)

            return need_coin

        dfs(root)
        return ans
