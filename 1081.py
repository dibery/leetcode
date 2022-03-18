class Solution:
    def smallestSubsequence(self, s: str) -> str:
        pos = {}
        ans = ''
        for seq, c in enumerate(s):
            pos.setdefault(c, []).append(seq)
        while pos:
            for k in sorted(pos.keys()):
                if all(pos[p][-1] >= pos[k][0] for p in pos):
                    ans += k
                    for i in pos:
                        while pos[i][0] < pos[k][0]:
                            pos[i].pop(0)
                    del pos[k]
                    break
        return ans
