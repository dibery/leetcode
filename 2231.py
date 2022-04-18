class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        o, e = [], []
        for n in num:
            if n in '02468':
                e.append(n)
            else:
                o.append(n)
        o.sort()
        e.sort()
        ans = ''
        for n in num:
            if int(n) % 2 == 0:
                ans += e[-1]
                e.pop()
            else:
                ans += o[-1]
                o.pop()
        return int(ans)
