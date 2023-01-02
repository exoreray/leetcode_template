# 1. Stack (“Last-in, first-out”)
		
        # a. Use list
        
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.pop()
			
		
        # b. Use queue

from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
queue.pop()  