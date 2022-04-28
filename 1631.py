from queue import SimpleQueue as Q
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        def ok(val):
            vis = set()
            bfs = Q()
            bfs.put((0, 0))
            vis.add((0, 0))
            while bfs.qsize():
                now = bfs.get()
                if now[0] == H - 1 and now[1] == W - 1:
                    return True
                for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    next = (now[0] + d[0], now[1] + d[1])
                    if H > next[0] >= 0 and W > next[1] >= 0 and \
                        abs(heights[now[0]][now[1]] - heights[next[0]][next[1]]) <= val and \
                        next not in vis:
                        bfs.put(next)
                        vis.add(next)
            return False
        l, h = 0, max(max(i) for i in heights)
        while l < h:
            test = (l + h) // 2
            if ok(test):
                h = test
            else:
                l = test + 1
        return l
