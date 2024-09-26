# 297. Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:
# def serialize(self, root):
#     """Encodes a tree to a single string.

#     :type root: TreeNode
#     :rtype: str
#     """


# def deserialize(self, data):
#     """Decodes your encoded data to tree.

#     :type data: str
#     :rtype: TreeNode
#     """


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        def makingdata(root):
            if not root:
                return "#"
            return (
                str(root.val)
                + ","
                + makingdata(root.left)
                + ","
                + makingdata(root.right)
            )

        return makingdata(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if not data:
            return
        data = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if i >= len(data):
                return
            if data[i] == "#":
                i += 1
                return

            root = TreeNode(data[i])
            i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
