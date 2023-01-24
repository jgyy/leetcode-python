from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, out = divmod(v1 + v2 + carry, 10)
            if head is None:
                head = tail = ListNode(out)
            else:
                tail.next = ListNode(out)
                tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head
    
    def printValue(self, value: Optional[ListNode]) -> List[int]:
        lis = [value.val]
        nodeNext = value.next
        while isinstance(nodeNext, ListNode):
            lis.append(nodeNext.val)
            nodeNext = nodeNext.next
        return lis


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3, ListNode(5))))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(3))))
    value = Solution().addTwoNumbers(l1, l2)
    print(Solution().printValue(value))
