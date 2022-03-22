import string
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = 'a' * ((26 * n - k) // 25)
        k -= len(ans)
        if k % 26:
            ans += string.ascii_lowercase[k % 26 - 1]
        ans += 'z' * (k // 26)
        return ans
