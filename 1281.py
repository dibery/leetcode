import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, str(n)))
        return numpy.prod(n) - sum(n)
