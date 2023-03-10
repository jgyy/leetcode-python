from typing import List

# Segment tree node


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        def buildTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = buildTree(nums, l, mid)
            root.right = buildTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = buildTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateTree(root, index, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if index <= mid:
                updateTree(root.left, index, val)
            else:
                updateTree(root.right, index, val)
            root.total = root.left.total + root.right.total
        updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def sumRangeTree(root, left, right):
            if root.start == left and root.end == right:
                return root.total
            mid = (root.start + root.end) // 2
            if right <= mid:
                return sumRangeTree(root.left, left, right)
            elif left >= mid + 1:
                return sumRangeTree(root.right, left, right)
            else:
                return sumRangeTree(root.left, left, mid) + sumRangeTree(root.right, mid + 1, right)
        return sumRangeTree(self.root, left, right)


if __name__ == '__main__':
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
