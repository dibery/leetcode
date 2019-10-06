class Solution:
    def dfs(self, grid, i, j, s):
        grid[i][j] *= -1
        self.ans = max(self.ans, s)
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if (i == m) != (j == n) and len(grid) > m >= 0 and len(grid[0]) > n >= 0 and grid[m][n] > 0:
                    self.dfs(grid, m, n, s + grid[m][n])
        grid[i][j] *= -1

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        [self.dfs(grid, i, j, grid[i][j]) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]]
        return self.ans
