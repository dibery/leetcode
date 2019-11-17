class Solution:
    def remove(self, s, front, back):
        t, p = '', 0
        for i in s:
            if i == front:
                p, t = p + 1, t + i
            elif i == back:
                if p:
                    p, t = p - 1, t + i
            else:
                t += i
        return t
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.remove(s, '(', ')')[::-1]
        return self.remove(s, ')', '(')[::-1]
