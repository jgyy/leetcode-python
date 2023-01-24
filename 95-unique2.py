from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
            return all_trees
        return generate(1, n) if n else []
    
    def printTree(self, root: Optional[TreeNode]) -> List[str]:
        return (root.left, root.val, root.right) if root else None


if __name__ == "__main__":
    s = Solution()
    print(list(map(s.printTree, s.generateTrees(3))))
