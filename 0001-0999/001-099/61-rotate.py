from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        for _ in range(n - k % n):
            head = head.next
            tail = tail.next
        tail.next = None
        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    print(Solution().rotateRight(head, k).val)
