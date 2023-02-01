from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(Solution().kthSmallest(root, 1))
    print(Solution().kthSmallest(root, 2))
    print(Solution().kthSmallest(root, 3))
    print(Solution().kthSmallest(root, 4))
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(Solution().kthSmallest(root, 3))
    print(Solution().kthSmallest(root, 4))
    print(Solution().kthSmallest(root, 5))
    print(Solution().kthSmallest(root, 6))
