class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = -int(x[::-1][:-1]) if x[0] == '-' else int(x[::-1])
        return 0 if x >= 2 ** 31 or x < -(2 ** 31) else x
