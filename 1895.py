from numpy import *
def ok(grid):
    row = set(grid.sum(axis=0))
    col = set(grid.sum(axis=1))
    d1 = diag(grid).sum()
    d2 = diag(grid[:,::-1]).sum()
    return len(row) == len(col) == 1 and sum(list(row)) == sum(list(col)) == d1 == d2
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        grid = array(grid)
        for size in range(min(grid.shape), 1, -1):
            for i in range(len(grid) - size + 1):
                for j in range(len(grid[0]) - size + 1):
                    if ok(grid[i:i + size,j:j + size]):
                        return size
        return 1
