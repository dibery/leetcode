class Solution:
    def gcd(self, a, b):
        return self.gcd(b, a % b) if a % b else b
    def lcm2(self, a, b):
        return a * b // self.gcd(a, b)
    def lcm3(self, a, b, c):
        return self.lcm2(a, self.lcm2(b, c))
    def hasUgly(self, n, a, b, c):
        return n // a + n // b + n // c - n // self.lcm2(a, b) - n // self.lcm2(a, c) - n // self.lcm2(b, c) + n // self.lcm3(a, b, c)
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        L, M, R = 1, 1000000000, 2000000000
        while R - L > 5:
            if self.hasUgly(M, a, b, c) >= n:
                R = M
                M = (L + R) // 2
            elif self.hasUgly(M, a, b, c) < n:
                L = M
                M = (L + R) // 2
        for i in range(L, R + 1):
            if self.hasUgly(i, a, b, c) == n:
                return i
