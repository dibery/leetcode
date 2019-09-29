from math import inf
from bisect import *

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        old, new = [arr1[0], min(arr1[0], arr2[0])], []
        for i in range(1, len(arr1)):
            new = [arr1[i] if arr1[i] > old[0] else inf]
            for j in range(1, i + 1):
                new.append(min(arr2[bisect_right(arr2, old[j - 1])] if arr2[-1] > old[j - 1] else inf, arr1[i] if arr1[i] > old[j] else inf))
            new.append(arr2[bisect_right(arr2, old[-1])] if arr2[-1] > old[-1] else inf)
            old = new
        for i in range(len(old)):
            if old[i] != inf:
                return i
        return -1
