from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(node):
            if node:
                dfs(node.left)
                if len(res) == k:
                    if abs(node.val - target) < abs(res[0] - target):
                        res.pop(0)
                    else:
                        return
                res.append(node.val)
                dfs(node.right)
        res = []
        dfs(root)
        return res


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    print(Solution().closestKValues(root, 3.714286, 2))
