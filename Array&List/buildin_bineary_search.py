from ast import List
from sortedcontainers import SortedList

'''
this build in function use balance bst
'''
l = SortedList()

l.add(9)
l.add(8)
l.add(7)
l.add(5)
l.add(5)
l.add(5)
l.add(3)
l.add(2)
l.add(1)
l.add(0)
'''
l = [0,1,2,3,5,5,5,7,8,9]
i = [0,1,2,3,4,5,6,7,8,9]
'''
print(l.bisect_left(0))
print(l.bisect_left(5)) # return the index of the first 5 (the place to insert 5 on the left)
print(l.bisect_right(5)) # return the index of the last 5 + 1 (the place to insert 5 on the right)
print(l.count(5)) # count how many 5s are there
print(l.index(1)) 
print(l.index(5)) # return the idnex of first 5

class Solution:
    def reversePairs(self, nums):
        l = SortedList()
        result = []
        for n in reversed(nums):
            result.insert(0, l.bisect_left(n))
            l.add(n)
        return sum(result)