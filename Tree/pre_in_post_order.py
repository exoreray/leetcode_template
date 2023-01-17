from define import TreeNode 

# recursion

def traverse(root):
    if not root:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置


# iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            p = stack.pop()
            res.append(p.val)
            # 看右子树
            p = p.right
        return res
