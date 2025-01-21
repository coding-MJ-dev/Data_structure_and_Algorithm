# 894. All Possible Full Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode()]}

        for nodes in range(2, n+1):
            val = []
            for rootnode in range(1, nodes):
                left = dp[rootnode - 1]
                right = dp[nodes - rootnode]
                for lt in left:
                    for rt in right:
                        val.append(TreeNode(0, lt, rt))
            dp[nodes] = val
        
        # print(dp)
        return dp[n]
    


    

        # dp = {0: [], 1: [TreeNode(0)]}

        # def dfs(n):
        #     if n in dp:
        #         return dp[n]
            
        #     ans = []
        #     for root in range(2, n+1):
        #         left = root - 1
        #         right = n - root
        #         leftTrees = dfs(left)
        #         rightTrees = dfs(right)
        #         for lt in leftTrees:
        #             for rt in rightTrees:
        #                 ans.append(TreeNode(0, lt, rt))
        #     dp[n] = ans
        #     return ans
        
        # return dfs(n)
