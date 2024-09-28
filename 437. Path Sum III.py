# 437. Path Sum III


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        dic = {0: 1}
        ans = 0

        def dfs(root, curSum):
            nonlocal ans
            if not root:
                return 0

            curSum += root.val
            if curSum - targetSum in dic:
                ans += dic[curSum - targetSum]
            dic[curSum] = dic.get(curSum, 0) + 1
            dfs(root.left, curSum)
            dfs(root.right, curSum)
            dic[curSum] -= 1

        dfs(root, 0)
        return ans
