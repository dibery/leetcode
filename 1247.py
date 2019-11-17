class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = y = 0
        for i in zip(s1, s2):
            x += 1 if i == ('x', 'y') else 0
            y += 1 if i == ('y', 'x') else 0
        return -1 if (x + y) % 2 else x // 2 + y // 2 + x % 2 + y % 2
