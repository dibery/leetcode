import numpy

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        grid = numpy.array(grid)
        row, col = grid.sum(axis=1), grid.sum(axis=0)
        return grid.sum() - sum(row[i] == col[j] == grid[i][j] == 1 for i in range(len(row)) for j in range(len(col)))
