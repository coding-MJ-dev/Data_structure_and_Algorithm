# 142. Linked List Cycle 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and slow == fast:
                break

        if not fast or not fast.next:
            return

        check = head
        while check != slow:
            check = check.next
            slow = slow.next

        return check