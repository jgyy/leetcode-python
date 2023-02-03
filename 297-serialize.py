# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Your Codec object will be instantiated and called as such:
    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if not node:
                res.append("null")
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != "null":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    ans = vars(deser.deserialize(ser.serialize(root)))
    print(ans)
