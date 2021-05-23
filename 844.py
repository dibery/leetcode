class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = len(S) - 1, len(T) - 1
        while max(s, t) >= 0:
            back_s = back_t = 0
            if S[s] == '#':
                while True:
                    if S[s] == '#':
                        back_s -= 1
                    else:
                        back_s += 1
                    if back_s == 1 or s == -1:
                        break
                    s -= 1
            if T[t] == '#':
                while True:
                    if T[t] == '#':
                        back_t -= 1
                    else:
                        back_t += 1
                    if back_t == 1 or t == -1:
                        break
                    t -= 1
            if s == t == -1:
                return True
            if s == -1 or t == -1 or S[s] != T[t]:
                return False
            s, t = s - 1, t - 1
        return True
