from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if target < root.val else root.right
        return res


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    target = 3.714286
    print(Solution().closestValue(root, target))
