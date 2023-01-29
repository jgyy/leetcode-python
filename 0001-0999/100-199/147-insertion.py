from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        while cur:
            pre = dummy
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next, pre.next, cur = pre.next, cur, cur.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    headList = []
    head = Solution().insertionSortList(node1)
    while head:
        headList.append(head.val)
        head = head.next
    print(headList)
