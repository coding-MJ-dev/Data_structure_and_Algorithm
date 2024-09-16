# 24. Swap Nodes in Pairs


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        slow = first = head
        fast = second = head.next
        while fast and fast.next:
            slow_next = slow.next.next
            fast_next = fast.next.next

            slow.next = slow_next
            fast.next = fast_next

            slow = slow.next
            fast = fast.next

        slow.next = None

        cur = root = ListNode(0, second)
        slow = second
        fast = first
        while slow:
            slow_next = slow.next
            fast_next = fast.next

            cur.next = slow
            cur = cur.next
            cur.next = fast
            cur = cur.next

            slow = slow_next
            fast = fast_next

        return root.next
