class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.ans = {}
        def walk(pos, step, size):
            if pos in [-1, size] or pos > step:
                return 0
            if step == 1:
                return 1
            if (pos, step) in self.ans:
                return self.ans[pos, step]
            self.ans[pos, step] = val = (walk(pos - 1, step - 1, size) + walk(pos + 1, step - 1, size) + walk(pos, step - 1, size)) % 1000000007
            return val
        return walk(0, steps, arrLen)
