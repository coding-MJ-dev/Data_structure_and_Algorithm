# 2130. Maximum Twin Sum of a Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        seen = []

        slow = fast = head
        while fast and fast.next:
            seen.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        res = 0
        while slow:
            res = max(res, slow.val + seen.pop())
            slow = slow.next

        return res
