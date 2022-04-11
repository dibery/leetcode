import numpy
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid = numpy.array(grid)
        return numpy.roll(grid.flatten(), k).reshape(grid.shape)
