from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    S = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'B':
                    B = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'T':
                    T = (i, j)
                    grid[i][j] = '.'
                    
        def outside(pos):
            return pos[0] >= R or pos[0] < 0 or pos[1] >= C or pos[1] < 0 or grid[pos[0]][pos[1]] == '#'
        
        bfs, next_bfs, way = deque([(S, B)]), deque(), [(1, 0), (0, 1), (0, -1), (-1, 0)]
        R, C, dist, vis = len(grid), len(grid[0]), 1, set([(S, B)])
        
        while bfs:
            while bfs:
                S, B = bfs.popleft()
                for w in way:
                    Sn = (S[0] + w[0], S[1] + w[1])
                    if outside(Sn):
                        continue
                    if Sn != B and (Sn, B) not in vis:
                        bfs.append((Sn, B))
                        vis.add((Sn, B))
                    elif Sn == B:
                        Bn = (B[0] + w[0], B[1] + w[1])
                        if outside(Bn) or (Sn, Bn) in vis:
                            continue
                        if Bn == T:
                            return dist
                        elif (Sn, Bn) not in vis:
                            next_bfs.append((Sn, Bn))
                            vis.add((Sn, Bn))
            bfs, next_bfs, dist = next_bfs, deque(), dist + 1
            
        return -1
