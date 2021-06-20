class Solution:
    def dfs(self, g1, g2, r, c):
        g2[r][c] = 0
        self.bad |= not g1[r][c]
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + i < len(g1) and 0 <= c + j < len(g1[0]) and g2[r + i][c + j]:
                self.dfs(g1, g2, r + i, c + j)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid2[r][c]:
                    self.bad = False
                    self.dfs(grid1, grid2, r, c)
                    ans += not self.bad
        return ans
