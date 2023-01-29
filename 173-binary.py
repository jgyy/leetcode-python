from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # Your BSTIterator object will be instantiated and called as such:
    # obj = BSTIterator(root)
    # param_1 = obj.next()
    # param_2 = obj.hasNext()
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.current = root

    def next(self) -> int:
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        self.current = self.stack.pop()
        val = self.current.val
        self.current = self.current.right
        return val

    def hasNext(self) -> bool:
        return self.current or self.stack


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    iterator = BSTIterator(root)
    print(iterator.next())    # return 3
    print(iterator.next())    # return 7
    print(iterator.hasNext()) # return True
    print(iterator.next())    # return 9
    print(iterator.hasNext()) # return True
    print(iterator.next())    # return 15
    print(iterator.hasNext()) # return True
    print(iterator.next())    # return 20
    print(iterator.hasNext()) # return False
