# 143. Reorder List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        back_start = slow.next
        slow.next = None

        def reverse(node):
            pre = None
            cur = node

            while cur:
                pre, pre.next, cur = cur, pre, cur.next
            return pre

        back_start = reverse(back_start)

        front = head
        back = back_start

        while back:
            back_next = back.next
            front_next = front.next

            front.next = back
            back.next = front_next

            back = back_next
            front = front_next

        return head
