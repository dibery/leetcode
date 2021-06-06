class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        max_size = min(len(grid) + 1, len(grid[0]) + 1) // 2
        ans = set()
        for i in grid:
            for j in i:
                ans.add(j)
        for l in range(2, max_size + 1):
            for cx in range(l - 1, len(grid) - l + 1):
                for cy in range(l - 1, len(grid[0]) - l + 1):
                    s = grid[cx - l + 1][cy] + grid[cx + l - 1][cy]
                    for dx in range(-l + 2, l - 1):
                        s += grid[cx + dx][cy + l - 1 - abs(dx)] + grid[cx + dx][cy - l + 1 + abs(dx)]
                    ans.add(s)
        ans = sorted(ans, reverse=True)
        return ans if len(ans) <= 3 else ans[:3]