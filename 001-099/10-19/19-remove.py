from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l2 = ListNode(1, ListNode(3))
    l3 = ListNode(1, ListNode(2))
    print(Solution().removeNthFromEnd(l1, 2).val)
    print(Solution().removeNthFromEnd(l2, 1).val)
    print(Solution().removeNthFromEnd(l3, 1).val)
