class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = [False] * 51
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                cover[i] = True
        for i in range(left, right + 1):
            if not cover[i]:
                return False
        return True
