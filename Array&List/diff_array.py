# 370. Range Addition
from ast import List
from itertools import accumulate


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0]*(length + 1)
        for update in updates:
            diff[update[0]] += update[2]
            diff[update[1] + 1] -= update[2] # cautious, when -update, need to be one index afterward.
        return list(accumulate(diff))[:-1] # accumulate function efficiently reconstruct diff_array back. Last index is redundant.
        