import numpy, heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = numpy.zeros((len(points), len(points)), dtype=int)
        pq = [(0, 0)]
        vis = [False for i in points]
        cost = 0
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                d[i, j] = abs(x[0] - y[0]) + abs(x[1] - y[1])
        while pq:
            top = heapq.heappop(pq)
            if vis[top[1]]:
                continue
            cost += top[0]
            vis[top[1]] = True
            for i in range(len(points)):
                if not vis[i]:
                    heapq.heappush(pq, (d[top[1], i], i))
        return cost
