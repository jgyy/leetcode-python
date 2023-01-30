from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(
        6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(vars(Solution().removeElements(head, 6)))
