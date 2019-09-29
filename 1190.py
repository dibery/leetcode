class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        begin = len(s) - 1
        while begin >= 0:
            if s[begin] == '(':
                end = s.index(')', begin)
                s[begin] = s[end] = ''
                for i in range(1, (end - begin) // 2 + 1):
                    s[begin + i], s[end - i] = s[end - i], s[begin + i]
            begin -= 1
        return ''.join(s)
