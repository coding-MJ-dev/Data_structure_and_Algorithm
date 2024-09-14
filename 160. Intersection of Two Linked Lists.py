# 160. Intersection of Two Linked Lists


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return
        seen = {}
        count = 0
        while headA:
            seen[headA] = count
            count += 1
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return
