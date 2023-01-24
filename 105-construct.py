from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root

    def printTree(self, root: Optional[TreeNode]) -> List[int]:
        treeList = [root.val]
        checkTree = root
        while isinstance(checkTree.left, TreeNode) or isinstance(checkTree.right, TreeNode):
            treeList.append(checkTree.left.val)
            treeList.append(checkTree.right.val)
            if checkTree.left:
                checkTree = checkTree.left
                continue
            if checkTree.right:
                checkTree = checkTree.right
                continue
        return treeList if root else None


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    value = Solution().buildTree(preorder, inorder)
    print(Solution().printTree(value))
