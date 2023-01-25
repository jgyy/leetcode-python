from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None and targetSum - root.val == 0:
            return [[root.val]]
        return [[root.val] + path for path in self.pathSum(root.left, targetSum - root.val)] + [[root.val] + path for path in self.pathSum(root.right, targetSum - root.val)]


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    print(Solution().pathSum(root, targetSum))
