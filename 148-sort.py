from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        h = res = ListNode()
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next


if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    headList = []
    head = Solution().sortList(node1)
    while head:
        headList.append(head.val)
        head = head.next
    print(headList)
