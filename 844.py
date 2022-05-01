class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next(s, back=0):
            for i in range(len(s))[::-1]:
                if s[i] == '#':
                    back += 1
                elif back == 0:
                    yield s[i]
                else:
                    back -= 1
            yield ''
        return all(a == b for a, b in zip(*map(get_next, (s, t))))
