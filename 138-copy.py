from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            node.next = Node(node.val, node.next)
            node = node.next.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node, new_head, new_node = head, head.next, head.next
        while node:
            node.next = node.next.next
            node = node.next
            if new_node.next:
                new_node.next = new_node.next.next
                new_node = new_node.next
        return new_head


if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    print(vars(Solution().copyRandomList(node1)))
