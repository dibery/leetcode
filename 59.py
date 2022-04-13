import itertools, numpy
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = numpy.zeros((n, n), dtype=int)
        num = itertools.count(1)
        for seq, l in enumerate(range(n, 0, -2)):
            if l == 1:
                m[seq, seq] = next(num)
            for i in range(l - 1):
                m[seq, seq + i] = next(num)
            for i in range(l - 1):
                m[seq + i, seq + l - 1] = next(num)
            for i in range(l - 1):
                m[seq + l - 1, seq + l - 1 - i] = next(num)
            for i in range(l - 1):
                m[seq + l - 1 - i, seq] = next(num)
        return m
