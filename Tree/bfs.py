target = 0

def BFS2(node):
    queue = [node] 
    level = 0 

    while queue:
        new_queue = [] # diff: use new queue to seperate levels
        for curr in queue: 

            if curr == target:    
                """do some thing here when find target"""
                return 

            for neighbor in curr.neighbors:     
                new_queue.append(neighbor) # diff
        queue = new_queue # diff
        level += 1 