import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dij, dis = [(0, k - 1)], [None] * n
        e = [{} for i in range(n)]
        for t in times:
            e[t[0] - 1][t[1] - 1] = t[2]
        while dij:
            t = heapq.heappop(dij)
            if dis[t[1]] is None:
                dis[t[1]] = t[0]
            else:
                continue
            for i in e[t[1]]:
                if dis[i] is None:
                    heapq.heappush(dij, (t[0] + e[t[1]][i], i))
        return -1 if None in dis else max(dis)
