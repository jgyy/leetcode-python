from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, length):
            if not node:
                return length
            length = length + 1 if node.val == parent + 1 else 1
            return max(length, dfs(node.left, node.val, length), dfs(node.right, node.val, length))

        return dfs(root, root.val - 1, 0) if root else 0


if __name__ == '__main__':
    print(Solution().longestConsecutive(
        TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, None, TreeNode(5))))))
    assert Solution().longestConsecutive(
        TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, None, TreeNode(5))))) == 3
