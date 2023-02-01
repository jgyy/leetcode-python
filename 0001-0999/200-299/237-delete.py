# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.node = None

    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        self.node = node


if __name__ == '__main__':
    node = ListNode(4)
    node.next = ListNode(5)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)
    Solution().deleteNode(node.next)
    while node:
        print(node.val)
        node = node.next
