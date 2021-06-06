from collections import deque
from bisect import bisect
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        pack = sorted(packages)
        for i in range(len(boxes)):
            boxes[i] = sorted(boxes[i])
            
        prefix_sum = [0]
        for i in pack:
            prefix_sum.append(i + prefix_sum[-1])
            
        def calc(self, pack, box, ps):
            if pack[-1] > box[-1]:
                return 10 ** 19
            waste = next = last = 0
            for i in box:
                if i < pack[next]:
                    continue
                next = bisect(pack, i)
                waste += i * (next - last) - ps[next] + ps[last]
                last = next
                if next == len(pack):
                    break
            return waste
        
        ans = min(calc(self, pack, i, prefix_sum) for i in boxes)
        return ans % (10 ** 9 + 7) if ans != 10 ** 19 else -1
