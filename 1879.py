class Solution:
    def __init__(self):
        self.ans = {}
    def minimumXORSum(self, a: List[int], b: List[int], pos = 0, used = 0) -> int:
        if pos == len(a):
            self.ans[used] = 0
        if used in self.ans:
            return self.ans[used]
        for i in range(len(a)):
            if used & 1 << i == 0 and (a[pos] ^ b[i]) + \
                    self.minimumXORSum(a, b, pos + 1, used | 1 << i) < self.ans.get(used, 1e9):
                self.ans[used] = (a[pos] ^ b[i]) + self.ans[used | 1 << i]
        return self.ans[used]