class Solution:
    def ok(self, s, p, r, front):
        for idx in r[:front]:
            s[idx] = ' '
        ps = pp = 0
        while True:
            while ps < len(s) and s[ps] != p[pp]:
                ps += 1
            pp += 1
            if ps == len(s):
                return False
            ps += 1
            if pp == len(p):
                return True
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        L, M, H = 0, len(removable) // 2, len(removable) + 1
        while H - L > 5:
            if self.ok(list(s), p, removable, M):
                L = M
            else:
                H = M
            M = (L + H) // 2
        for i in range(L, H)[::-1]:
            if self.ok(list(s), p, removable, i):
                return i
