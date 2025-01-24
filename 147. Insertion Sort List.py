# 147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(-float('inf'))
        check = head
        while check:
            next_check = check.next
            pre, cur = root, root.next
            while cur and cur.val < check.val:
                pre = cur
                cur = cur.next
            pre.next = check
            check.next = cur
            check = next_check
        
        return root.next