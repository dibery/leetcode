class Solution:
    def perm(self, n):
        ans = 1
        for i in range(1, n + 1):
            ans = ans * i % int(1e9 + 7)
        return ans
    def numPrimeArrangements(self, n: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        p = [i for i in prime if i <= n]
        return self.perm(len(p)) * self.perm(n - len(p)) % int(1e9 + 7)
