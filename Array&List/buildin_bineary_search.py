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

print(l.bisect_left(0))
print(l.bisect_left(5))
print(l.bisect_right(5))
print(l.count(5))
print(l.index(1))
print(l.index(5))

class Solution:
    def reversePairs(self, nums):
        l = SortedList()
        result = []
        for n in reversed(nums):
            result.insert(0, l.bisect_left(n))
            l.add(n)
        return sum(result)