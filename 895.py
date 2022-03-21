from sortedcontainers import SortedDict as sd
class FreqStack:

    def __init__(self):
        self.pos = {}
        self.freq = {}
        self.invfreq = sd()
        self.seq = 0

    def push(self, val: int) -> None:
        self.seq += 1
        f = self.freq.setdefault(val, 0)
        if f:
            self.invfreq[f].pop(self.pos[val][-1])
        self.invfreq.setdefault(f + 1, sd())[self.seq] = val
        self.freq[val] = f + 1
        self.pos.setdefault(val, []).append(self.seq)

    def pop(self) -> int:
        #print(self.invfreq)
        pos, val = self.invfreq.peekitem()[1].peekitem()
        freq = self.invfreq.peekitem()[0]
        self.pos[val].pop()
        self.freq[val] -= 1
        self.invfreq[freq].pop(pos)
        if not self.invfreq[freq]:
            self.invfreq.pop(freq)
        if self.pos[val]:
            self.invfreq.setdefault(freq - 1, sd())[self.pos[val][-1]] = val
        return val
