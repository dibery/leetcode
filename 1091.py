import itertools
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        L = len(grid)
        d = [[0] * L for i in range(L)]
        bfs = collections.deque([] if grid[0][0] else [(0, 0)])
        d[0][0] = -1 if grid[0][0] else 1
        while bfs:
            t = bfs.popleft()
            for dir in itertools.product((-1, 0, 1), (-1, 0, 1)):
                if any(dir) and L > t[0] + dir[0] >= 0 and L > t[1] + dir[1] >= 0 and d[t[0] + dir[0]][t[1] + dir[1]] == grid[t[0] + dir[0]][t[1] + dir[1]] == 0:
                    bfs.append((t[0] + dir[0], t[1] + dir[1]))
                    d[t[0] + dir[0]][t[1] + dir[1]] = d[t[0]][t[1]] + 1
        return -1 if d[-1][-1] == 0 and L != 1 else d[-1][-1]
