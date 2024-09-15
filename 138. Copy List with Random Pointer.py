# 138. Copy List with Random Pointer


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return

        cur = head
        while cur:
            copy = Node(cur.val)
            nxt = cur.next
            cur.next = copy
            copy.next = nxt
            cur = nxt

        cur = head
        while cur and cur.next:
            if cur.random != None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        copy = copy_head = head.next
        while copy and copy.next:
            cur_next = cur.next.next
            copy_next = copy.next.next

            cur.next = cur_next
            copy.next = copy_next
            cur = cur.next
            copy = copy.next

        return copy_head
