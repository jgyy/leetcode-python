from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(vars(Solution().reverseList(head)))
