from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next

    def printValue(self, value: Optional[ListNode]) -> List[int]:
        lis = [value.val]
        nodeNext = value.next
        while isinstance(nodeNext, ListNode):
            lis.append(nodeNext.val)
            nodeNext = nodeNext.next
        return lis


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    value = s.reverseBetween(head, 2, 4)
    print(s.printValue(value))
