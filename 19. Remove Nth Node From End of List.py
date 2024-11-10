# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = root = ListNode(0, head)
        fast = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            pre.next = pre.next.next
            return pre.next
        
        cur = head
        
        while fast and fast.next:
            fast = fast.next
            cur = cur.next
        
        cur.next = cur.next.next

        return head