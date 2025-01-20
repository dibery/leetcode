class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos = {mat[i][j]: (i, j) for i in range(len(mat)) for j in range(len(mat[0]))}
        r, c = [0] * len(mat), [0] * len(mat[0])
        for i, n in enumerate(arr):
            r[pos[n][0]] += 1
            c[pos[n][1]] += 1
            if r[pos[n][0]] == len(mat[0]) or c[pos[n][1]] == len(mat):
                return i
