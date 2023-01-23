from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.val == head.next.val:
            while head.next is not None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    print(s.deleteDuplicates(head1).val)
    head2 = ListNode(1, ListNode(2, ListNode(
        3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    print(s.deleteDuplicates(head2).val)
    head3 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    print(s.deleteDuplicates(head3).val)
