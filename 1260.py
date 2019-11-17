import numpy

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        k %= R * C
        grid = numpy.array(grid).flatten().tolist()
        grid = numpy.array(grid[-k:] + grid[:-k])
        return grid.reshape(R, C)
