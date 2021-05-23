class Solution:
    def numSteps(self, s: str) -> int:
        s, ans = int(s, 2), 0
        while s > 1:
            ans += 1
            s += 1 if s % 2 else s //= 2
        return ans
