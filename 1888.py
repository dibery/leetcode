class Solution:
    def minFlips(self, s: str) -> int:
        def count(self, s, z_start):
            move = 0
            for seq, c in enumerate(s):
                if int(c) == (seq + int(z_start)) % 2:
                    move += 1
            return move
        if len(s) % 2 == 0:
            return min(count(self, s, True), count(self, s, False))
        else:
            F = [[None] * len(s) + [0] for i in 'zz']
            B = [[None] * len(s) + [0] for i in 'zz']
            for i in range(len(s)):
                if i == 0:
                    F[0][i] = int(s[0] != '0')
                    F[1][i] = int(s[0] == '0')
                else:
                    F[0][i] = F[0][i-1] + int(int(s[i]) != i % 2)
                    F[1][i] = F[1][i-1] + int(int(s[i]) == i % 2)
            
            for i in range(len(s))[::-1]:
                if i == len(s) - 1:
                    B[0][i] = int(s[i] != '0')
                    B[1][i] = int(s[i] == '0')
                else:
                    B[0][i] = B[0][i+1] + int(int(s[i]) != i % 2)
                    B[1][i] = B[1][i+1] + int(int(s[i]) == i % 2)
                    
            return min(min(F[0][i] + B[1][i+1], F[1][i] + B[0][i+1]) for i in range(len(s)))
