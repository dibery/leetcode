class Solution:
    def brokenCalc(self, s: int, t: int) -> int:
        ans = 0
        while s != t:
            if t < s:
                ans, t = ans + s - t, s
            elif t % 2:
                ans, t = ans + 1, t + 1
            else:
                ans, t = ans + 1, t // 2
        return ans
