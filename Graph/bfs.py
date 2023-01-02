target = 0

def BFS1(node):
    queue = [node] 
    visited = set(node) 
    level = 0 

    while queue:
        layer_size = len(queue) # diff: use size to seperate levels

        for _ in range(layer_size): 
            curr = queue.pop(0) # diff

            if curr == target:    
                """do some thing here when find target"""
                return 

            for neighbor in curr.neighbors:     
                if neighbor not in visited:
                    queue.append(neighbor) # diff
                    visited.add(neighbor)
        level += 1 
        
def BFS2(node):
    queue = [node] 
    visited = set(node) 
    level = 0 

    while queue:
        new_queue = [] # diff: use new queue to seperate levels
        for curr in queue: 

            if curr == target:    
                """do some thing here when find target"""
                return 

            for neighbor in curr.neighbors:     
                if neighbor not in visited:
                    new_queue.append(neighbor) # diff
                    visited.add(neighbor)
        queue = new_queue # diff
        level += 1 











##############################################################################################

target = 0


def BFS(node):
    queue = [node] # 核心数据结构 将起点加入队列
    visited = set(node) # 避免走回头路
    level = 0 # 记录目前所在层数

    while queue:
        layer_size = len(queue)
        for _ in range(layer_size): # 将当前队列中的所有节点向四周扩散 
            curr = queue.pop(0) 
            if curr == target:    # 判断是否到达终点
                """do some thing here when find target"""
                return 

            for neighbor in curr.neighbors:     # 将 curr 的相邻节点加入队列
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        level += 1 # 更新层数