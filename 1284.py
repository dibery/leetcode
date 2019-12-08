class Solution:
    def sol(self, mat, first):
        mat, move = [i.copy() for i in mat], 0
        for j in range(len(mat)):
            for i in range(len(mat[0])):
                if (j and mat[j - 1][i]) or (not j and 1 << i & first):
                    move += 1
                    if j > 0:
                        mat[j - 1][i] ^= 1
                    if j + 1 < len(mat):
                        mat[j + 1][i] ^= 1
                    if i > 0:
                        mat[j][i - 1] ^= 1
                    if i + 1 < len(mat[0]):
                        mat[j][i + 1] ^= 1
                    mat[j][i] ^= 1
        return 1e9 if sum(sum(i) for i in mat) else move
    def minFlips(self, mat: List[List[int]]) -> int:
        ans = min(self.sol(mat, i) for i in range(2 ** len(mat[0])))
        return -1 if ans == 1e9 else ans
