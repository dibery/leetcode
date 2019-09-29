class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        ps = {}
        for i in lower:
            l = [0]
            for c in s:
                l.append(l[-1] + (0 if c != i else 1))
            ps[i] = l
        ans = []
        for q in queries:
            b, e, m = q
            e += 1
            stat = [ps[i][e] - ps[i][b] for i in lower]
            c = len([x for x in stat if x % 2 == 1])
            if ( e - b ) % 2 == 1:
                c -= 1
            ans.append(True if c <= 2 * m and c % 2 == 0 else False)
        return ans