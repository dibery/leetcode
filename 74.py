from bisect import bisect_left
class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        r = bisect_left(m, t, key=lambda i: i[-1])
        return m[r][bisect_left(m[r], t)] == t if r < len(m) else False
