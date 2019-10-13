from collections import Counter
class Solution:
    def maxEqualFreq(self, num: List[int]) -> int:
        cnt, fcnt, uniqf, ans = Counter(), [set() for i in range(len(num) + 1)], set(), 0
        for i in range(len(num)):
            fcnt[cnt[num[i]]].discard(num[i])
            if not fcnt[cnt[num[i]]]:
                uniqf.discard(cnt[num[i]])
            cnt[num[i]] += 1
            fcnt[cnt[num[i]]].add(num[i])
            uniqf.add(cnt[num[i]])
            if len(uniqf) == 2 and ((len(fcnt[max(uniqf)]) == 1 and max(uniqf) - min(uniqf) == 1) or len(fcnt[1]) == 1) or len(uniqf) == 1 and (1 in uniqf or len(fcnt[list(uniqf)[0]]) == 1):
                ans = i
        return ans + 1
