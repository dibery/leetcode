class Solution:
    def minimizeResult(self, e: str) -> str:
        val = 1e11
        ans = ''
        e = e.split('+')
        for i in range(len(e[0])):
            for j in range(1, len(e[1]) + 1):
                ca = cd = False
                a, b = e[0][:i], e[0][i:]
                c, d = e[1][:j], e[1][j:]
                #print(f'{a},{b},{c},{d}')
                if not a:
                    a = '1'
                    ca = True
                if not d:
                    d = '1'
                    cd = True
                #print(int(a) * (int(b) + int(c)) * int(d))
                if int(a) * (int(b) + int(c)) * int(d) <= val:
                    val = int(a) * (int(b) + int(c)) * int(d)
                    if ca:
                        a = ''
                    if cd:
                        d = ''
                    ans = f'{a}({b}+{c}){d}'
        return ans
