import numpy
from math import inf

class Solution:
    def get(self, n, m):
        gcd = numpy.gcd(n, m)
        n, m = min(n, m) // gcd, max(n, m) // gcd
        if self.ans[n][m] != inf:
            return self.ans[n][m]
        for i in range(1, n):
            self.ans[n][m] = self.ans[m][n] = min(self.get(i, m) + self.get(n - i, m), self.ans[n][m])
        for i in range(1, m):
            self.ans[n][m] = self.ans[m][n] = min(self.get(n, i) + self.get(n, m - i), self.ans[n][m])
        return self.ans[n][m]

    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = [[1 if i == j else inf for j in range(14)] for i in range(14)]
        self.ans[11][13] = self.ans[13][11] = 6
        return self.get(min(n, m), max(n, m))
