from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pred = None
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                    continue
                else:
                    pre.right = None
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val
        self.root = root

    def printTree(self, root: Optional[TreeNode]) -> List[str]:
        def v(value: int | None | TreeNode) -> int | None:
            val = value
            while isinstance(val, TreeNode):
                val = val.val
            return val
        return (v(root.left), v(root.val), v(root.right)) if root else None


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    s.recoverTree(root)
    print(s.printTree(root))
