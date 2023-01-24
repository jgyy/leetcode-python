from typing import Optional, List

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

    def printValue(self, value: Optional[ListNode]) -> List[int]:
        lis = [value.val]
        nodeNext = value.next
        while isinstance(nodeNext, ListNode):
            lis.append(nodeNext.val)
            nodeNext = nodeNext.next
        return lis


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    value = Solution().removeNthFromEnd(l1, 2)
    print(Solution().printValue(value))
