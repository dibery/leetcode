class Solution:
    def countVowelPermutation(self, n: int) -> int:
        ans, dep = [[1] for i in range(5)], [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        for i in range(1, n):
            for j in range(5):
                ans[j].append(sum(ans[k][i - 1] for k in dep[j]))
        return sum(i[-1] for i in ans) % 1000000007
