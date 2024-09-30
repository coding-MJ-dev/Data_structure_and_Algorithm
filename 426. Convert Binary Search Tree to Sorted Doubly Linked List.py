# 426. Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return
        pre_node = None
        head = None

        def dfs(node):
            nonlocal head, pre_node
            if node:

                if node.left:
                    dfs(node.left)

                if head == None:
                    head = Node(0, left=node)
                    pre_node = head
                node.left = pre_node
                pre_node.right = node
                pre_node = node

                if node.right:
                    dfs(node.right)

        dfs(root)
        pre_node.right = head.right
        head.right.left = pre_node

        return head.right
