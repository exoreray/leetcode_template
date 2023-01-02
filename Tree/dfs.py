target = 0

def DFS_tree(node):
    if node == target:    
        """do some thing here when find target"""
        return 
    DFS_tree(node.left)
    DFS_tree(node.right)
    return