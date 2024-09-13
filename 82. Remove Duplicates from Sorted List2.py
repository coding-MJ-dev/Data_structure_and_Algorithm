# 82. Remove Duplicates from Sorted List2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # better way
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next


# I did it
# root = dummy = ListNode(-1, head)
# prev = None
# cur = head
# while cur:
#     if cur.next and cur.val == cur.next.val:
#         prev = cur.val
#         cur = cur.next
#     else:
#         if cur.val == prev:
#             if cur.next:
#                 cur = cur.next
#             else:
#                 root.next = None
#                 cur = cur.next
#         else:
#             root.next = cur
#             prev = cur.val

#             root = root.next
#             cur = cur.next
# return dummy.next
