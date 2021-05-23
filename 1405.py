class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        while a + b + c:
            if a >= b and a >= c and not ans.endswith('aa'):
                use = min(1 + int(not ans.endswith('a')), a)
                ans += 'a' * use
                a -= use
                if b >= c and b:
                    ans += 'b'
                    b -= 1
                elif c:
                    ans += 'c'
                    c -= 1
                else:
                    return ans
            elif b >= a and b >= c and not ans.endswith('bb'):
                use = min(1 + int(not ans.endswith('b')), b)
                ans += 'b' * use
                b -= use
                if a >= c and a:
                    ans += 'a'
                    a -= 1
                elif c:
                    ans += 'c'
                    c -= 1
                else:
                    return ans
            elif not ans.endswith('cc'):
                use = min(1 + int(not ans.endswith('c')), c)
                ans += 'c' * use
                c -= use
                if b >= a and b:
                    ans += 'b'
                    b -= 1
                elif a:
                    ans += 'a'
                    a -= 1
                else:
                    return ans
        return ans
