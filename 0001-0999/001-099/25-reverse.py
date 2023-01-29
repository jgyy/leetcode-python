from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: ListNode, tail: ListNode):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head

        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().reverseKGroup(l1, 2).val)
    print(Solution().reverseKGroup(l2, 3).val)
    print(Solution().reverseKGroup(l3, 1).val)
