from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        head = point = ListNode(0)
        for v in sorted(vals):
            point.next = ListNode(v)
            point = point.next
        return head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    print(Solution().mergeKLists([l1, l2, l3]).val)
