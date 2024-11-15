# 337. House Robber III



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return (0, 0)
            
            left_rob, without_left_rob = dfs(root.left)
            right_rob, without_right_rob = dfs(root.right)
            rob = (root.val + without_left_rob + without_right_rob, max(left_rob, without_left_rob) + max(right_rob, without_right_rob))

            return rob
        
        return max(dfs(root))




        # def dfs(node):
        #     if not node:
        #         return [0, 0] # with rob, without rob
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     withRob = node.val + left[1] + right[1]
        #     withoutRob = max(left) + max(right)

        #     return [withRob, withoutRob]
        
        # return max(dfs(root))

