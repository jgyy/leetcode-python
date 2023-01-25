from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))


if __name__ == "__main__":
    head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    value = Solution().sortedListToBST(head)
    print(vars(value))
