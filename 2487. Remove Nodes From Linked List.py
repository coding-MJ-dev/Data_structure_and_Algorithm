# 2487. Remove Nodes From Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            pre = None
            cur = node
            while cur:
                pre, pre.next, cur = cur, pre, cur.next
            return pre

        cur = head = reverse(head)

        while cur and cur.next:
            if cur.next.val < cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return reverse(head)