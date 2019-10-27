from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        l, each = len(s), len(s) // 4
        start, end = 0, l - 1
        c = Counter()
        while start < l:
            if c[s[start]] == each:
                break
            c[s[start]] += 1
            start += 1
        ans = l - start
        start -= 1
        while end >= start >= -1:
            while end >= start >= -1 and c[s[end]] == each:
                if start == -1:
                    return ans
                c[s[start]] -= 1
                start -= 1                
            c[s[end]] += 1
            end -= 1
            ans = min(ans, end - start)
        return ans
