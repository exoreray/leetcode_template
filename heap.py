# Python code to demonstrate working of heapify(), heappush() and heappop()
 
# importing "heapq" to implement heap queue
import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(li)             # for a min heap
heapq._heapify_max(li)        # for a maxheap!!
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
 
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
 
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
 
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
print (heapq._heappop_max(li))

