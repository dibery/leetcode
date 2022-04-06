from collections import Counter
import math
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        a, ans = Counter(arr), 0
        def calc(c):
            return math.prod(math.comb(a[k], c[k]) for k in c)
        for i in range(target // 3 + 1):
            for j in range(i, (target - i) // 2 + 1):
                ans += calc(Counter((i, j, target - i - j)))
        return ans % 1000000007
