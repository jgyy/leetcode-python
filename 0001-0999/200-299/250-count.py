from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, True
            if not node.left and not node.right:
                return 1, True
            left_count, left_uni = dfs(node.left)
            right_count, right_uni = dfs(node.right)
            if not left_uni or not right_uni:
                return left_count + right_count, False
            if node.left and node.left.val != node.val:
                return left_count + right_count, False
            if node.right and node.right.val != node.val:
                return left_count + right_count, False
            return left_count + right_count + 1, True

        return dfs(root)[0]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)),
                    TreeNode(5, None, TreeNode(5)))
    print(s.countUnivalSubtrees(root))
