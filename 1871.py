class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        def one(n):
            return (1 << n) - 1
        mask = (one(maxJump) ^ one(minJump - 1)) << 1
        
        S = int(''.join(map(lambda i: str(1 ^ int(i)), s[::-1])), 2)
        bfs = 1
        while bfs:
            pos = bfs & -bfs
            bfs -= pos
            bfs |= (mask * pos) & S
            if bfs >> len(s) - 1:
                return True
        return False