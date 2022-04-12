import scipy.signal, itertools
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = scipy.signal.convolve(board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], 'same')
        for r, c in itertools.product(range(len(board)), range(len(board[0]))):
            board[r][c] = board[r][c] & (3 >= n[r,c] >= 2) | (n[r,c] == 3)
