# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i < size - 1:
                    node.next = queue[0]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return root


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    Solution().connect(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.left.val)
    print(root.right.right.val)
