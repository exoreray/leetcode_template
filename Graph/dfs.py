target = 0


visited = set() 
onPath = [] 

def DFS(node): 

    if node in onPath:
        # hasCycle = True
        return 
    
    if node in visited:
        return

    if node == target:    
        """do some thing here when find target"""
        return 

    visited.add(node) 
    onPath.append(node) 

    for neighbor in node.neighbors:
        DFS(neighbor)

    onPath.pop() 












##############################################################################################




target = 0


visited = set() # 记录被遍历过的节点
onPath = [] # 记录从起点到当前节点的路径

def DFS(node): # 图遍历框架 
    if node in visited:
        return
    if node == target:    # 判断是否到目标
        """do some thing here when find target"""
        return 

    visited.add(node) # 经过节点 s，标记为已遍历
    onPath.append(node) # 做选择：标记节点 s 在路径上
    for neighbor in node.neighbors:
        DFS(neighbor)
    onPath.pop() # 撤销选择：节点 s 离开路径