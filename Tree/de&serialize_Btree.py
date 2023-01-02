# 前序遍历法

# Definition for a binary tree node.
from re import T


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        result = str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right) 
        return result  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if type(data) is str:
            data = data.split(" ")
        if not data or data[0] == "#":
            data.pop(0)
            return None
        val = data.pop(0)
        node = TreeNode(val)
        node.left = self.deserialize(data)
        node.right = self.deserialize(data)
        return node

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(4)
print(serialized_tree := ser.serialize(root))
deserialized = deser.deserialize(serialized_tree)

def preorder(root, vals):
        if root.val is not None:
            vals.append(root.val)
        if root.left is not None:
            preorder(root.left, vals)
        if root.right is not None:
            preorder(root.right, vals)
        return vals

print("preorder:")
print(preorder(deserialized, []))
# 后序遍历法

# BFS法
