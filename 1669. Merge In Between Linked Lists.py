# 1669. Merge In Between Linked Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        cur = list1
        for _ in range(a - 1):
            cur = cur.next

        second = cur
        for _ in range(b - a + 2):
            second = second.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        cur.next = second

        return list1
