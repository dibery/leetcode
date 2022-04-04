class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pan(begin, end):
            while begin < end and s[begin] == s[end]:
                begin, end = begin + 1, end - 1
            return begin >= end, begin, end
        ok, b, e = pan(0, len(s) - 1)
        return ok or pan(b + 1, e)[0] or pan(b, e - 1)[0]