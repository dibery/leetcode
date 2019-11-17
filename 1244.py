class Leaderboard:

    def __init__(self):
        self.record = {}

    def addScore(self, playerId: int, score: int) -> None:
        try:
            self.record[playerId] += score
        except:
            self.record[playerId] = score

    def top(self, K: int) -> int:
        return sum(sorted(self.record.values())[-K:])

    def reset(self, playerId: int) -> None:
        self.record[playerId] = 0
