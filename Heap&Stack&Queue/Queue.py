# 2. Queue (“First-in, first-out”)

    # a. Use list

queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.pop(0)
		
        
    # b. Use queue

from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
queue.popleft() 