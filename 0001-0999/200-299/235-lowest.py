# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print(Solution().lowestCommonAncestor(root, root.left, root.right).val)
    print(Solution().lowestCommonAncestor(root, root.left, root.left.right).val)
    print(Solution().lowestCommonAncestor(root, root.left, root.left.right.left).val)
    print(Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val)
    print(Solution().lowestCommonAncestor(root, root.right, root.right.left).val)
    print(Solution().lowestCommonAncestor(root, root.right, root.right.right).val)
