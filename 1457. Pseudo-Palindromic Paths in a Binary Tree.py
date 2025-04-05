# 1457. Pseudo-Palindromic Paths in a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ## Using bit manipulation
        def dfs(node, mask):
            if not node:
                return 0
            
            mask ^= (1 << node.val)

            if not node.left and not node.right:
                return 1 if (mask & (mask -1)) == 0 else 0
            
            return dfs(node.left, mask) + dfs(node.right, mask)
        
        return dfs(root, 0)
            




# Using Counter


        # dic = defaultdict(int)
        # odd = 0
        # def dfs(node):
        #     nonlocal odd
        #     if not node:
        #         return 0

        #     dic[node.val] += 1
        #     odd_change = 1 if dic[node.val] % 2 == 1 else -1
        #     odd += odd_change
            
        #     val = 0
        #     if not node.left and not node.right:
        #         val = 1 if odd <= 1 else 0

        #     else:
        #         val = dfs(node.left) + dfs(node.right)
            
        #     dic[node.val] -= 1
        #     odd -= odd_change
            
        #     return val
        
        # return dfs(root)