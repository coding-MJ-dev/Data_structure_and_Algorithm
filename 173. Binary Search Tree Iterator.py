# 173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.hp = []
        # heapq.heapify(self.hp)

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.hp.append(root.val)
            dfs(root.right)

        dfs(root)
        print(self.hp)

    def next(self) -> int:
        if self.hp:
            return heappop(self.hp)
        else:
            return -1

    def hasNext(self) -> bool:
        if self.hp:
            return True
        else:
            return False
