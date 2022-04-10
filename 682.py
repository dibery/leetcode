class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for op in ops:
            try:
                s.append(int(op))
            except:
                if op == '+':
                    s.append(s[-1] + s[-2])
                elif op == 'D':
                    s.append(s[-1] * 2)
                else:
                    s.pop()
        return sum(s)
