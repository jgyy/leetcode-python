from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)),
                    TreeNode(3, None, TreeNode(4)))
    print(Solution().rightSideView(root))
