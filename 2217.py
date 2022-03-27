class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        zpan = [10 ** ((i + 1) // 2) for i in range(14)]
        ans = []
        for q in queries:
            if intLength < 3:
                ans.append(int(str(q) * intLength) if q < 10 else -1)
            elif q > 9 * zpan[intLength - 2]:
                ans.append(-1)
            else:
                s = '123456789'[(q - 1) // zpan[intLength - 2]]
                s += f'%0{(intLength - 1) // 2}d' % ((q - 1) % zpan[intLength - 2])
                s += s[:-1][::-1] if intLength % 2 else s += s[::-1]
                ans.append(int(s))
        return ans