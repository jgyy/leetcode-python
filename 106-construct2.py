from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return root

    def printTree(self, root: Optional[TreeNode]) -> List[int]:
        treeList = [root.val]
        checkTree = root
        while isinstance(checkTree.left, TreeNode) and isinstance(checkTree.right, TreeNode):
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