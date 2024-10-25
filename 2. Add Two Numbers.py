# 2. Add Two Numbers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 졸업
        carry = 0
        root = ListNode()
        cur = root
        while l1 or l2 or carry:
            if l1 and l2:
                carry, val = divmod(l1.val + l2.val + carry, 10)
                cur.next = ListNode(val)
                cur = cur.next
                l1 = l1.next
                l2 = l2.next

            elif l1:
                carry, val = divmod(l1.val + carry, 10)
                cur.next = ListNode(val)
                cur = cur.next
                l1 = l1.next

            elif l2:
                carry, val = divmod(l2.val + carry, 10)
                cur.next = ListNode(val)
                cur = cur.next
                l2 = l2.next

            else:
                cur.next = ListNode(carry)
                carry = 0
                cur = cur.next

        return root.next
