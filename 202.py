class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        n = str(n)
        while n not in vis:
            vis.add(n)
            n = str(sum(map(lambda i: int(i) ** 2, n)))
        return '1' in vis
