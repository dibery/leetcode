class Solution:
    def fight(self, player, p1, p2, depth = 1):
        if (player.index(p1), player.index(p2), depth) in self.found:
            return
        self.found.add((player.index(p1), player.index(p2), depth))
        for i in range(2 ** (len(player) // 2)):
            Next = [] if len(player) % 2 == 0 else [player[len(player) // 2]]
            for j in range(len(player) // 2):
                if set([player[j], player[-j - 1]]) == set([p1, p2]):
                    self.m = min(self.m, depth)
                    self.M = max(self.M, depth)
                    break
                Next.append(player[j] if 1 << j & i else player[-j - 1])
            if p1 not in Next or p2 not in Next:
                continue
            self.fight(sorted(Next), p1, p2, depth + 1)
    def earliestAndLatest(self, n: int, p1: int, p2: int) -> List[int]:
        self.m, self.M, self.found = 5, 1, set()
        self.fight(list(range(n)), p1-1, p2-1)
        return [self.m, self.M]
