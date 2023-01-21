from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        while point and point.next:
            point.val, point.next.val = point.next.val, point.val
            point = point.next.next
        return head


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().swapPairs(l1).val)
