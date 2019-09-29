class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        bfs, dist = [(0, 0, True)], {(0, 0, True): 0}
        while bfs:
            now = bfs.pop(0)
            R, C, H = now
            if H:
                if C + 2 < len(grid[0]) and not grid[R][C + 2]:
                    self.update(dist, bfs, (R, C + 1, H), dist[now] + 1)
                if R + 1 < len(grid) and 1 not in grid[R + 1][C:C + 2]:
                    self.update(dist, bfs, (R + 1, C, H), dist[now] + 1)
                    self.update(dist, bfs, (R, C, not H), dist[now] + 1)
            else:
                if C + 1 < len(grid[0]) and not grid[R][C + 1] and not grid[R + 1][C + 1]:
                    self.update(dist, bfs, (R, C + 1, H), dist[now] + 1)
                    self.update(dist, bfs, (R, C, not H), dist[now] + 1)
                if R + 2 < len(grid) and not grid[R + 2][C]:
                    self.update(dist, bfs, (R + 1, C, H), dist[now] + 1)
        return dist.get((len(grid) - 1, len(grid[0]) - 2, True), -1)
    
    def update(self, dist, bfs, node, val):
        if node not in dist:
            dist[node] = val
            bfs.append(node)
