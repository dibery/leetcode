class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        ans = [[0] * (k + 1) for p in piles]
        for i in range(1, min(k, len(piles[0])) + 1):
            ans[0][i] = ans[0][i - 1] + piles[0][i - 1]
        ps = len(piles[0])
        for i in range(1, len(piles)):
            ps += len(piles[i])
            for j in range(1, min(ps, k) + 1):
                prefix = 0
                best = ans[i - 1][j]
                for m in range(min(len(piles[i]), j)):
                    prefix += piles[i][m]
                    best = max(best, prefix + ans[i - 1][j - m - 1])
                ans[i][j] = best
        return ans[len(piles) - 1][k]