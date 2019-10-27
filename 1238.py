class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = ['0', '1']
        for i in range(1, n):
            gray = ['0' + i for i in gray] + ['1' + i for i in gray[::-1]]
        gray = [int(i, 2) for i in gray]
        pos = gray.index(start)
        return gray[pos:] + gray[:pos]
