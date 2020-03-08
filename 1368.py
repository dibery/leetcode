from heapq import *
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        W, H, dij, way = len(grid[0]), len(grid), [(0, 0, 0)], [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[None] * W for i in range(H)]
        while dij:
            d, y, x = heappop(dij)
            if dist[y][x] != None:
                continue
            dist[y][x] = d
            for w in range(len(way)):
                nx, ny = x + way[w][1], y + way[w][0]
                if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] == None:
                    heappush(dij, (d + (0 if w == grid[y][x] - 1 else 1), ny, nx))
        return dist[-1][-1]