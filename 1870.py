from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def getTime(dist, speed):
            return dist[-1] / speed + sum(ceil(i / speed) for i in dist[:-1])
        if getTime(dist, 10 ** 7) > hour:
            return -1
        low, high = 1, 10 ** 7
        while (high - low >= 5):
            mid = (low + high) / 2
            if getTime(dist, mid) <= hour:
                high = mid
            else:
                low = mid
        for i in range(int(low), int(ceil(high) + 1)):
            if i and getTime(dist, i) <= hour:
                return i