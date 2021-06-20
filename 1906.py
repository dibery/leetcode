from bisect import *
class Solution:
    def find(self, pos, l, r):
        for diff in range(1, 100):
            for s in range(1, 101 - diff):
                S = bisect_left(pos[s], l)
                E = bisect_left(pos[s + diff], l)
                if S < len(pos[s]) and E < len(pos[s + diff]) and pos[s][S] <= r and pos[s + diff][E] <= r:
                    return diff
        return -1
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pos = [[] for i in range(101)]
        for seq, n in enumerate(nums):
            pos[n].append(seq)
        return [self.find(pos, l, r) for l, r in queries]
