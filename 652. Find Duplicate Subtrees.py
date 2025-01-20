# 652. Find Duplicate Subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        dp = defaultdict(int)

        def dfs(root):
            if not root:
                return '#'
            
            val = f"{root.val},{dfs(root.left)},{dfs(root.right)}"
            dp[val] += 1
            if dp[val] == 2:
                ans.append(root)
            return val

        dfs(root)
        # print(dp)
        return ans








        # dp = defaultdict(list)
        # ans = []
        
        # def dfs(node):
        #     if not node:
        #         return "N"
            
        #     key = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
        #     if len(dp[key]) == 1:
        #         ans.append(node)
        #     dp[key].append(node)
        #     return key
        
        # dfs(root)
        # return ans
            