from bisect import bisect
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prefix = [0]
        for i in range(len(s)):
            prefix.append(prefix[-1] + abs(ord(s[i]) - ord(t[i])))
        return max(bisect(prefix, maxCost + prefix[i]) - 1 - i for i in range(len(s)))
